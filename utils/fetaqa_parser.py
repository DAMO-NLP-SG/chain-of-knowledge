import json
import random
import sqlite3
from typing import List

import pandas as pd
from datasets import load_dataset
from nltk import sent_tokenize
from pydantic import BaseModel

from utils.knowl_query import retrieve_knowledge
from utils.openai_utils import call_openai_api
from utils.other_prompts import (
    fetaqa_s1_prompt_demonstration,
    fetaqa_s2_edit_prompt_demonstration,
    fetaqa_query_demonstration,
    fetaqa_query_s2_demonstration,
    fetaqa_standard_demonstration,
    fetaqa_query_standard_demonstration,
    fetaqa_no_table_demonstration,
    fetaqa_sql_wiki_demonstration,
    fetaqa_cot_demonstration,
)
from utils.retrieval.wikipedia import execute_wikipedia_query


class TableArray(BaseModel):
    values: List[list]

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame):
        values = [df.columns.tolist()]
        for row in df.values:
            values.append(row.tolist())
        return cls(values=values)

    def as_dataframe(self) -> pd.DataFrame:
        df = pd.DataFrame(self.values[1:], columns=self.values[0])
        df = df.loc[:, ~df.columns.duplicated()]
        for key in df.keys():
            try:
                df[key] = pd.to_numeric(df[key])
            except Exception as e:
                assert e is not None

        return df

    def run_query(self, query: str):
        df = self.as_dataframe()
        conn = sqlite3.connect(":memory:")
        query = query.replace("table", "my_table")
        df.to_sql("my_table", conn, index=False)
        result = pd.read_sql_query(query, conn)
        conn.close()
        return self.from_dataframe(result)


class FetaQADataset:
    def __init__(
        self,
        num_sample: int = 500,
        random_seed: int = 0,
        max_table_rows: int = 10,
        num_train: int = 0,
    ):
        random.seed(random_seed)
        self.data = [raw for raw in load_dataset("DongfuTingle/FeTaQA", split="test")]
        self.data = random.sample(self.data, k=num_sample)
        self.question_map = {raw["question"]: raw for raw in self.data}
        self.s1_prompt_demonstration = fetaqa_s1_prompt_demonstration
        self.max_table_rows = max_table_rows
        self.num_train = num_train

    def process_demonstration(self, prompt: str, sep="\n\n") -> str:
        parts = prompt.split(sep)
        assert len(parts) in [4, 7], "Only support 3 and 6-shot in other_prompts.py"
        assert self.num_train > 0
        parts = parts[: self.num_train + 1]
        assert len(parts) == self.num_train + 1
        return sep.join(parts).strip()

    def get_dataset(self) -> List[dict]:
        return self.data

    def get_question(self, data_point):
        return data_point["question"]

    def get_ground_truth(self, data_point):
        return data_point["answer"]

    def get_s1_prompt(self, question):
        data = self.question_map[question]
        table = data["table_array"][: self.max_table_rows]
        prefix = f"The table is about {data['table_section_title']} of {data['table_page_title']}."
        return f"{self.s1_prompt_demonstration.strip()}\nTable: {table}\nQ: {prefix} {question.strip()}\nA:"

    def get_s2_edit_prompt(self, rationale, rationale_knowledge):
        raise NotImplementedError

    def get_s3_consolidation_prompt(self, question, rationale_1, rationale_2):
        raise NotImplementedError

    def get_cot_sc_results(self, data_point, model, cot_prompt):
        cot_sc_responses = call_openai_api(
            model, cot_prompt, max_tokens=256, temperature=0.7, n=10
        )

        if cot_sc_responses is not None:
            all_cot_text_response = [
                x["message"]["content"].strip() for x in cot_sc_responses[0]["choices"]
            ]  # for chat models
            # all_cot_text_response = [x["text"].strip() for x in cot_sc_responses[0]["choices"]] # for text models

            all_cot_results = []

            prefix = "Thus,"
            for x in all_cot_text_response:
                if prefix in x:
                    all_cot_results.append(x.split(prefix)[1].strip().lower())
                else:
                    all_cot_results.append(x.strip().lower())

            all_cot_results = all_cot_results[:5]

            # find the most common answer and indices in all_cot_results
            most_common_answer = max(set(all_cot_results), key=all_cot_results.count)
            most_common_answer_indices = [
                i for i, x in enumerate(all_cot_results) if x == most_common_answer
            ]

            sc_score = float(len(most_common_answer_indices)) / len(all_cot_results)

            # use the first answer as cot answer
            cot_answer = all_cot_results[0]

            cot_sc_text_response = all_cot_text_response[most_common_answer_indices[0]]
            cot_sc_answer = most_common_answer
            parts = sent_tokenize(cot_sc_text_response)
        else:
            raise Exception("Stage 1: OpenAI API call failed")

        # store the results
        data_point["cot_response"] = all_cot_text_response[0]
        data_point["cot_answer"] = cot_answer
        data_point["cot_sc_score"] = sc_score
        data_point["cot_sc_response"] = cot_sc_text_response
        data_point["cot_sc_answer"] = cot_sc_answer
        data_point["cot_sc_rationales"] = [] if len(parts) == 1 else parts[:-1]
        return data_point

    def update_rationales_step_by_step(self, model, data_point):
        raise NotImplementedError

    def update_rationales_at_once(self, data_point):
        raise NotImplementedError

    def get_final_answer(self, model, data_point):
        raise NotImplementedError


class FetaStandardDataset(FetaQADataset):
    def get_s1_prompt(self, question):
        data = self.question_map[question]
        table = data["table_array"][: self.max_table_rows]
        demo = self.process_demonstration(fetaqa_standard_demonstration)
        parts = [
            demo,
            "",
            f"Table: {table}",
            f"Q: {question}",
            "A:",
        ]
        return "\n".join(parts)

    def get_cot_sc_results(self, data_point, model, cot_prompt):
        responses = call_openai_api(model, cot_prompt, n=1)

        if responses is not None:
            _, pred = responses
            pred = pred.replace("A: ", "").strip().lower()
        else:
            raise Exception("Stage 1: OpenAI API call failed")

        # store the results
        data_point["cot_response"] = pred
        data_point["cot_answer"] = pred
        data_point["cot_sc_score"] = 1.0
        data_point["cot_sc_response"] = ""
        return data_point


class FetaCotDataset(FetaQADataset):
    def get_s1_prompt(self, question):
        data = self.question_map[question]
        table = data["table_array"][: self.max_table_rows]
        demo = self.process_demonstration(fetaqa_cot_demonstration)
        parts = [
            demo,
            "",
            f"Table: {table}",
            f"Q: {question}",
            "A:",
        ]
        return "\n".join(parts)

    def get_cot_sc_results(self, data_point, model, cot_prompt):
        responses = call_openai_api(model, cot_prompt, n=1)

        if responses is not None:
            _, pred = responses
            prefix = "Thus, "
            if prefix in pred:
                pred = pred.split(prefix)[1]
            pred = pred.strip().lower()
        else:
            raise Exception("Stage 1: OpenAI API call failed")

        # store the results
        data_point["cot_response"] = pred
        data_point["cot_answer"] = pred
        data_point["cot_sc_score"] = 1.0
        data_point["cot_sc_response"] = ""
        return data_point


class FetaNoTableDataset(FetaStandardDataset):
    def get_s1_prompt(self, question):
        demo = self.process_demonstration(fetaqa_no_table_demonstration)
        parts = [
            demo,
            "",
            f"Q: {question}",
            "A:",
        ]
        return "\n".join(parts)


class FetaQAWithQueryDataset(FetaQADataset):
    def get_sql_query(self, data: dict, model: str) -> str:
        question = data["question"]
        table = data["table_array"][: self.max_table_rows]
        prefix = f"The table is about {data['table_section_title']} of {data['table_page_title']}."
        demo = self.process_demonstration(fetaqa_query_demonstration)
        parts = [
            demo,
            "",
            f"Table: {table}",
            f"Question: {prefix} {question.strip()}",
            f"Columns: {table[0]}",
            "Query:",
        ]

        prompt = "\n".join(parts)
        _, query = call_openai_api(model, prompt)
        query = query.strip()
        if "Query:" in query:
            query = query.split("Query:")[0].strip()
        return query

    def get_query_s2_prompt(self, data: dict, query: str, result: List[list]):
        question = data["question"]
        table = data["table_array"][: self.max_table_rows]
        prefix = f"The table is about {data['table_section_title']} of {data['table_page_title']}."
        parts = [
            fetaqa_query_s2_demonstration.strip(),
            "",
            f"Table: {table}",
            f"Question: {prefix} {question.strip()}",
            f"Query: {query.strip()}",
            f"Result: {result}",
            "Answer:",
        ]
        return "\n".join(parts)

    def get_cot_sc_results(self, data_point, model, cot_prompt):
        del cot_prompt
        query = self.get_sql_query(data_point, model)
        try:
            array = TableArray(values=data_point["table_array"])
            result = array.run_query(query).values
        except Exception as e:
            print(e)
            result = data_point["table_array"][-5:]

        cot_prompt = self.get_query_s2_prompt(data_point, query, result)
        cot_sc_responses = call_openai_api(
            model, cot_prompt, max_tokens=256, temperature=0.7, n=10
        )

        if cot_sc_responses is not None:
            all_cot_text_response = [
                x["message"]["content"].strip() for x in cot_sc_responses[0]["choices"]
            ]  # for chat models
            # all_cot_text_response = [x["text"].strip() for x in cot_sc_responses[0]["choices"]] # for text models

            all_cot_results = []

            prefix = "Thus,"
            for x in all_cot_text_response:
                if prefix in x:
                    all_cot_results.append(x.split(prefix)[1].strip().lower())
                else:
                    all_cot_results.append(x.strip().lower())

            all_cot_results = all_cot_results[:5]

            # find the most common answer and indices in all_cot_results
            most_common_answer = max(set(all_cot_results), key=all_cot_results.count)
            most_common_answer_indices = [
                i for i, x in enumerate(all_cot_results) if x == most_common_answer
            ]

            sc_score = float(len(most_common_answer_indices)) / len(all_cot_results)

            # use the first answer as cot answer
            cot_answer = all_cot_results[0]

            cot_sc_text_response = all_cot_text_response[most_common_answer_indices[0]]
            cot_sc_answer = most_common_answer
            parts = sent_tokenize(cot_sc_text_response)
        else:
            raise Exception("Stage 1: OpenAI API call failed")

        # store the results
        data_point["cot_response"] = all_cot_text_response[0]
        data_point["cot_answer"] = cot_answer
        data_point["cot_sc_score"] = sc_score
        data_point["cot_sc_response"] = cot_sc_text_response
        data_point["cot_sc_answer"] = cot_sc_answer
        data_point["cot_sc_rationales"] = [] if len(parts) == 1 else parts[:-1]

        return data_point


class FetaQueryStandardDataset(FetaQAWithQueryDataset):
    def get_query_s2_prompt(self, data: dict, query: str, result: List[list]):
        question = data["question"]
        table = data["table_array"][: self.max_table_rows]
        prefix = f"The table is about {data['table_section_title']} of {data['table_page_title']}."
        demo = self.process_demonstration(fetaqa_query_standard_demonstration)
        parts = [
            demo,
            "",
            f"Table: {table}",
            f"Question: {prefix} {question.strip()}",
            f"Query: {query.strip()}",
            f"Result: {result}",
            "Answer:",
        ]
        return "\n".join(parts)

    def get_cot_sc_results(self, data_point, model, cot_prompt):
        del cot_prompt
        query = self.get_sql_query(data_point, model)
        try:
            array = TableArray(values=data_point["table_array"])
            result = array.run_query(query).values
        except Exception as e:
            print(e)
            result = data_point["table_array"][-5:]

        prompt = self.get_query_s2_prompt(data_point, query, result)
        responses = call_openai_api(model, prompt, n=1)
        data_point["prompt"] = prompt

        if responses is not None:
            _, pred = responses
            pred = pred.replace("Answer: ", "").strip().lower()
        else:
            raise Exception("Stage 1: OpenAI API call failed")

        # store the results
        data_point["cot_response"] = pred
        data_point["cot_answer"] = pred
        data_point["cot_sc_score"] = 1.0
        data_point["cot_sc_response"] = ""
        return data_point


class FetaSQLWikiDataset(FetaQueryStandardDataset):
    def get_query_s2_prompt(self, data: dict, query: str, result: List[list]):
        question = data["question"]
        table = data["table_array"][: self.max_table_rows]
        prefix = f"The table is about {data['table_section_title']} of {data['table_page_title']}."
        demo = self.process_demonstration(fetaqa_sql_wiki_demonstration)

        wiki_query = f"{data['table_section_title']} of {data['table_page_title']}. {question.strip()}"
        wiki_result = execute_wikipedia_query(wiki_query)
        context = sent_tokenize(wiki_result.replace("...", "").strip())[0].strip()
        info = dict(wiki_query=wiki_query, wiki_result=wiki_result, context=context)
        print(json.dumps(info, indent=2))

        parts = [
            demo,
            "",
            f"Table: {table}",
            f"Context: {context}",
            f"Question: {prefix} {question.strip()}",
            f"Query: {query.strip()}",
            f"Result: {result}",
            "Answer:",
        ]
        return "\n".join(parts)


class FetaQAWithEditingDataset(FetaQADataset):
    def get_s2_edit_prompt(self, rationale, rationale_knowledge):
        sentence = (
            fetaqa_s2_edit_prompt_demonstration
            + "Sentence: "
            + rationale
            + "\nKnowledge: "
        )
        for x in rationale_knowledge:
            for y in rationale_knowledge[x]:
                sentence += rationale_knowledge[x][y] + " "
        sentence += "\nEdited sentence: "
        return sentence

    def get_s3_consolidation_prompt(self, question, rationale_1, rationale_2):
        return (
            self.s1_prompt_demonstration
            + "Q: "
            + question.strip()
            + "\nA: First, "
            + rationale_1
            + " Second, "
            + rationale_2
            + " Thus, "
        )

    def update_rationales_step_by_step(self, model, data_point):
        domains = data_point["s1_domains"]
        rationales = [x.strip() for x in data_point["cot_sc_rationales"]]
        while len(rationales) < 2:
            rationales.append(
                self.get_question(data_point)
            )  # Placeholder to avoid errors
        rationale_1 = rationales[0]
        rationale_2 = rationales[1]

        print("****** Editing Rationale 1 ...")
        # retrieve knowledge for rationale 1 first
        rationale_1_knowl = retrieve_knowledge(domains, rationale_1, data_point)

        # edit rationale 1 based on rationale 1_knowl
        s2_edit_prompt_rationale_1 = self.get_s2_edit_prompt(
            rationale_1, rationale_1_knowl
        )
        # print(s2_edit_prompt_rationale_1)
        edited_rationale_1 = call_openai_api(
            model, s2_edit_prompt_rationale_1, max_tokens=256, temperature=0, n=1
        )[1].strip()
        print("*** Original rationale 1:", rationale_1)
        print("*** Edited rationale 1:", edited_rationale_1)

        print("****** Editing Rationale 2 ...")
        # generate rationale 2 using edited rationale 1
        new_rationale_2_prompt = (
            self.s1_prompt_demonstration
            + "Q: "
            + data_point["question"].strip()
            + "\nA: First, "
            + edited_rationale_1
            + " Second, "
        )
        # print(new_rationale_2_prompt)
        new_rationale_2 = call_openai_api(
            model, new_rationale_2_prompt, max_tokens=256, temperature=0, n=1
        )[1].strip()
        # get the rationale, remove the answer sentence
        new_rationale_2 = new_rationale_2.split("Thus,")[0].strip()
        print("*** New rationale 2:", new_rationale_2)

        data_point["rationale_1_knowl"] = rationale_1_knowl
        data_point["edited_rationale_1"] = edited_rationale_1
        data_point["new_rationale_2"] = new_rationale_2

        # retreive knowledge for rationale 2
        rationale_2_knowl = retrieve_knowledge(domains, new_rationale_2, data_point)

        # edit rationale 2 based on rationale 2_knowl
        s2_edit_prompt_rationale_2 = self.get_s2_edit_prompt(
            new_rationale_2, rationale_2_knowl
        )
        # print(s2_edit_prompt_rationale_2)
        edited_rationale_2 = call_openai_api(
            model, s2_edit_prompt_rationale_2, max_tokens=256, temperature=0, n=1
        )[1].strip()
        print("*** Original rationale 2:", rationale_2)
        print("*** Edited rationale 2:", edited_rationale_2)

        # store the results
        data_point["rationale_2_knowl"] = rationale_2_knowl
        data_point["edited_rationale_2"] = edited_rationale_2

        return data_point

    def get_final_answer(self, model, data_point):
        print(
            "****** Edited rationales: ",
            "First, "
            + data_point["edited_rationale_1"]
            + " Second, "
            + data_point["edited_rationale_2"],
        )
        s3_answer_consolidation_prompt = self.get_s3_consolidation_prompt(
            data_point["question"],
            data_point["edited_rationale_1"],
            data_point["edited_rationale_2"],
        )
        final_answer = call_openai_api(
            model, s3_answer_consolidation_prompt, max_tokens=256, temperature=0, n=1
        )[1].strip()
        data_point["final_answer"] = final_answer
        print("****** Final answer:", final_answer)
        print("****** Original answer:", data_point["cot_sc_answer"])
        print("****** Gold answer:", data_point["answer"])
        return data_point


def select_fetaqa_dataset(name: str, **kwargs):
    if name == "fetaqa":
        return FetaQADataset(**kwargs)
    if name == "fetaqa_query":
        return FetaQAWithQueryDataset(**kwargs)
    if name == "fetaqa_editing":
        return FetaQAWithEditingDataset(**kwargs)
    if name == "fetaqa_standard":
        return FetaStandardDataset(**kwargs)
    if name == "fetaqa_query_standard":
        return FetaQueryStandardDataset(**kwargs)
    if name == "fetaqa_no_table":
        return FetaNoTableDataset(**kwargs)
    if name == "fetaqa_sql_wiki":
        return FetaSQLWikiDataset(**kwargs)
    if name == "fetaqa_cot":
        return FetaCotDataset(**kwargs)
    raise KeyError(name)
