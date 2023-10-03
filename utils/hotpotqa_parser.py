import os
import json
from utils.openai_utils import call_openai_api
from utils.knowl_query import retrieve_knowledge
from utils.other_prompts import hotpotqa_s1_prompt_demonstration, hotpotqa_s2_edit_prompt_demonstration

class hotpotqa:
    def __init__(self):
        # load data
        with open("datasets/hotpotqa/simplified_data.json", "r") as f:
            self.data = json.load(f)
        
        # s1_prompt
        self.s1_prompt_demonstration = hotpotqa_s1_prompt_demonstration
        
        # s2_edit_prompt
        self.s2_edit_prompt_demonstration = hotpotqa_s2_edit_prompt_demonstration
        
    def get_dataset(self):
        return self.data
    
    def get_question(self, data_point):
        return data_point["question"]
    
    def get_ground_truth(self, data_point):
        return data_point["answer"]
    
    def get_s1_prompt(self, question):
        return self.s1_prompt_demonstration + "Q: " + question.strip() + "\nA: "

    def get_s2_edit_prompt(self, rationale, rationale_knowledge):
        sentence = self.s2_edit_prompt_demonstration + "Sentence: " + rationale + "\nKnowledge: "
        for x in rationale_knowledge:
            for y in rationale_knowledge[x]:
                sentence += rationale_knowledge[x][y] + " "
        sentence += "\nEdited sentence: "
        return sentence

    def get_s3_consolidation_prompt(self, question, rationale_1, rationale_2):
        return self.s1_prompt_demonstration + "Q: " + question.strip() + "\nA: First, " + rationale_1 + " Second, " + rationale_2 + " The answer is "
    
    def get_cot_sc_results(self, data_point, model, cot_prompt):
        cot_sc_responses = call_openai_api(model, cot_prompt, max_tokens=256, temperature=0.7, n=10)
    
        if cot_sc_responses is not None:
            
            all_cot_text_response = [x["message"]["content"].strip() for x in cot_sc_responses[0]["choices"]] # for chat models
            # all_cot_text_response = [x["text"].strip() for x in cot_sc_responses[0]["choices"]] # for text models
            
            all_cot_results = []
            
            for x in all_cot_text_response:
                if "The answer is" in x:
                    all_cot_results.append(x.split("The answer is")[1].strip().lower())
                else:
                    None
            
            all_cot_results = all_cot_results[:5]
            # all_cot_results = [x.split("The answer is")[1].strip().lower() for x in all_cot_text_response]
            
            # find the most common answer and indices in all_cot_results
            most_common_answer = max(set(all_cot_results), key = all_cot_results.count)
            most_common_answer_indices = [i for i, x in enumerate(all_cot_results) if x == most_common_answer]
            
            sc_score = float(len(most_common_answer_indices)) / len(all_cot_results)
            
            # use the first answer as cot answer
            cot_answer = all_cot_results[0]
            
            # cot_sc answer and rationales
            cot_sc_text_response = all_cot_text_response[most_common_answer_indices[0]]
            cot_sc_rationale_1 = cot_sc_text_response.split("Second, ")[0].strip().split("First, ")[1].strip()
            cot_sc_rationale_2 = cot_sc_text_response.split("Second, ")[1].strip().split("The answer is")[0].strip()
            cot_sc_answer = most_common_answer
        else:
            raise Exception("Stage 1: OpenAI API call failed")
        
        # store the results
        data_point["cot_response"] = all_cot_text_response[0]
        data_point["cot_answer"] = cot_answer
        data_point["cot_sc_score"] = sc_score
        data_point["cot_sc_response"] = cot_sc_text_response
        data_point["cot_sc_answer"] = cot_sc_answer
        data_point["cot_sc_rationales"] = [cot_sc_rationale_1, cot_sc_rationale_2]

        return data_point
    
    def update_rationales_step_by_step(self, model, data_point):
        domains = data_point["s1_domains"]
        rationales = [x.strip() for x in data_point["cot_sc_rationales"]]
        rationale_1 = rationales[0]
        rationale_2 = rationales[1]

        print("****** Editing Rationale 1 ...")
        # retrieve knowledge for rationale 1 first
        rationale_1_knowl = retrieve_knowledge(domains, rationale_1, data_point)

        # edit rationale 1 based on rationale 1_knowl
        s2_edit_prompt_rationale_1 = self.get_s2_edit_prompt(rationale_1, rationale_1_knowl)
        # print(s2_edit_prompt_rationale_1)
        edited_rationale_1 = call_openai_api(model, s2_edit_prompt_rationale_1, max_tokens=256, temperature=0, n=1)[1].strip()
        print("*** Original rationale 1:", rationale_1)
        print("*** Edited rationale 1:", edited_rationale_1)
        
        print("****** Editing Rationale 2 ...")
        # generate rationale 2 using edited rationale 1
        new_rationale_2_prompt = self.s1_prompt_demonstration + "Q: " + data_point["question"].strip() + "\nA: First, " + edited_rationale_1 + " Second, "
        # print(new_rationale_2_prompt)
        new_rationale_2 = call_openai_api(model, new_rationale_2_prompt, max_tokens=256, temperature=0, n=1)[1].strip()
        # get the rationale, remove the answer sentence
        new_rationale_2 = new_rationale_2.split("The answer is")[0].strip()
        print("*** New rationale 2:", new_rationale_2)
        
        data_point["rationale_1_knowl"] = rationale_1_knowl
        data_point["edited_rationale_1"] = edited_rationale_1
        data_point["new_rationale_2"] = new_rationale_2

        # retreive knowledge for rationale 2
        rationale_2_knowl = retrieve_knowledge(domains, new_rationale_2, data_point)

        # edit rationale 2 based on rationale 2_knowl
        s2_edit_prompt_rationale_2 = self.get_s2_edit_prompt(new_rationale_2, rationale_2_knowl)
        # print(s2_edit_prompt_rationale_2)
        edited_rationale_2 = call_openai_api(model, s2_edit_prompt_rationale_2, max_tokens=256, temperature=0, n=1)[1].strip()
        print("*** Original rationale 2:", rationale_2)
        print("*** Edited rationale 2:", edited_rationale_2)

        # store the results
        data_point["rationale_2_knowl"] = rationale_2_knowl
        data_point["edited_rationale_2"] = edited_rationale_2

        return data_point

        
    def update_rationales_at_once(self, data_point):
        domains = data_point["s1_domains"]
        rationales = [x.strip() for x in data_point["cot_sc_rationales"]]
        rationale_1 = rationales[0]
        rationale_2 = rationales[1]

        print("****** Editing Rationale 1 ...")
        # retrieve knowledge for rationale 1 first
        rationale_1_knowl = retrieve_knowledge(domains, rationale_1, data_point)

        # edit rationale 1 based on rationale 1_knowl
        s2_edit_prompt_rationale_1 = self.get_s2_edit_prompt(rationale_1, rationale_1_knowl)
        # print(s2_edit_prompt_rationale_1)
        edited_rationale_1 = call_openai_api(model, s2_edit_prompt_rationale_1, max_tokens=256, temperature=0, n=1)[1].strip()
        print("*** Original rationale 1:", rationale_1)
        print("*** Edited rationale 1:", edited_rationale_1)
        
        print("****** Editing Rationale 2 ...")        
        
        data_point["rationale_1_knowl"] = rationale_1_knowl
        data_point["edited_rationale_1"] = edited_rationale_1

        # retreive knowledge for rationale 2
        rationale_2_knowl = retrieve_knowledge(domains, rationale_2, data_point)

        # edit rationale 2 based on rationale 2_knowl
        s2_edit_prompt_rationale_2 = self.get_s2_edit_prompt(rationale_2, rationale_2_knowl)
        # print(s2_edit_prompt_rationale_2)
        edited_rationale_2 = call_openai_api(model, s2_edit_prompt_rationale_2, max_tokens=256, temperature=0, n=1)[1].strip()
        print("*** Original rationale 2:", rationale_2)
        print("*** Edited rationale 2:", edited_rationale_2)

        # store the results
        data_point["rationale_2_knowl"] = rationale_2_knowl
        data_point["edited_rationale_2"] = edited_rationale_2

        return data_point

    
    def get_final_answer(self, model, data_point):
        print("****** Edited rationales: ", "First, " + data_point["edited_rationale_1"] + " Second, " + data_point["edited_rationale_2"])
        s3_answer_consolidation_prompt = self.get_s3_consolidation_prompt(data_point["question"], data_point["edited_rationale_1"], data_point["edited_rationale_2"])
        final_answer = call_openai_api(model, s3_answer_consolidation_prompt, max_tokens=256, temperature=0, n=1)[1].strip()
        data_point["final_answer"] = final_answer
        print("****** Final answer:", final_answer)
        print("****** Original answer:", data_point["cot_sc_answer"])
        print("****** Gold answer:", data_point["answer"])
        return data_point
