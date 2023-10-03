import os
import json
from utils.openai_utils import call_openai_api
from utils.knowl_query import retrieve_knowledge, knowl_is_empty
from utils.other_prompts import fever_s1_prompt_demonstration, fever_s2_edit_prompt_demonstration, fever_s1_prompt_demonstration_6_shot, fever_s1_prompt_demonstration_1_shot

class fever:
    def __init__(self, six_shot = False, one_shot = False):
        # load data
        with open("datasets/fever/sampled_1000.json", "r") as f:
            self.data = json.load(f)
        for data_point in self.data:
            data_point['question'] = data_point['claim']
            data_point['answer'] = data_point['label']
        
        if one_shot:
            # s1_prompt
            self.s1_prompt_demonstration = fever_s1_prompt_demonstration_1_shot
            print('Intialized with 1-shot demonstration prompts')
        elif six_shot:
            # s1_prompt
            self.s1_prompt_demonstration = fever_s1_prompt_demonstration_6_shot
            print('Intialized with 6-shot demonstration prompts')
        else:
            # s1_prompt
            self.s1_prompt_demonstration = fever_s1_prompt_demonstration
            
        # s2_edit_prompt
        self.s2_edit_prompt_demonstration = fever_s2_edit_prompt_demonstration
            
        
    def get_dataset(self):
        return self.data
    
    def get_question(self, data_point):
        return data_point["claim"]
    
    def get_ground_truth(self, data_point):
        return data_point["label"]
    
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
            try:
                most_common_answer = max(set(all_cot_results), key = all_cot_results.count)
                most_common_answer_indices = [i for i, x in enumerate(all_cot_results) if x == most_common_answer]
            except Exception as e:
                print('all_cot_text_response: ', all_cot_text_response)
                print('all_cot_results: ', all_cot_results)
                raise e
            
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
        if knowl_is_empty(rationale_1_knowl):
            # edit rationale 1 based on rationale 1_knowl
            s2_edit_prompt_rationale_1 = self.get_s2_edit_prompt(rationale_1, rationale_1_knowl)
            # print(s2_edit_prompt_rationale_1)
            edited_rationale_1 = call_openai_api(model, s2_edit_prompt_rationale_1, max_tokens=256, temperature=0, n=1)[1].strip()
            print("*** Original rationale 1:", rationale_1)
            print("*** Edited rationale 1:", edited_rationale_1)
        else:
            print('No knowledge found for rationale 1')
            edited_rationale_1 = rationale_1
        
        print("****** Editing Rationale 2 ...")
        # generate rationale 2 using edited rationale 1
        new_rationale_2_prompt = self.s1_prompt_demonstration + "Q: " + self.get_question(data_point).strip() + "\nA: First, " + edited_rationale_1 + " Second, "
        print('new_rationale_2_prompt: ', new_rationale_2_prompt)
        new_rationale_2 = call_openai_api(model, new_rationale_2_prompt, max_tokens=256, temperature=0, n=1)[1].strip()
        # get the rationale, remove the answer sentence
        new_rationale_2 = new_rationale_2.split("The answer is")[0].strip()
        print("*** New rationale 2:", new_rationale_2)
        
        data_point["rationale_1_knowl"] = rationale_1_knowl
        data_point["edited_rationale_1"] = edited_rationale_1
        data_point["new_rationale_2"] = new_rationale_2

        # retreive knowledge for rationale 2
        rationale_2_knowl = retrieve_knowledge(domains, new_rationale_2, data_point)

        if knowl_is_empty(rationale_2_knowl):
            # edit rationale 2 based on rationale 2_knowl
            s2_edit_prompt_rationale_2 = self.get_s2_edit_prompt(new_rationale_2, rationale_2_knowl)
            print('s2_edit_prompt_rationale_2: ', s2_edit_prompt_rationale_2)
            edited_rationale_2 = call_openai_api(model, s2_edit_prompt_rationale_2, max_tokens=256, temperature=0, n=1)[1].strip()
            print("*** Original rationale 2:", rationale_2)
            print("*** Edited rationale 2:", edited_rationale_2)
        else:
            print('No knowledge found for rationale 2')
            edited_rationale_2 = new_rationale_2

        # store the results
        data_point["rationale_2_knowl"] = rationale_2_knowl
        data_point["edited_rationale_2"] = edited_rationale_2
        return data_point

        
    def update_rationales_at_once(self, model, data_point):
        # domains = data_point["s1_domains"]
        domains = ["factual"] # for ve
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

    def get_ans_text(self, text):
        if 'the answer is' in text.lower():
            text = text.lower().split('the answer is')[-1].strip()
        possible_answer_dict = {
            'REFUTES': ['refutes', 'refute', 'false', 'incorrect', 'not accurate', 'not true', 'not correct', 'does not make sense', 'not entirely accurate', 'incomplete'],
            'SUPPORTS': ['supports', 'support', 'true', 'correct'],
            'NOT ENOUGH INFO': ['not enough information', 'not enough info']
        }
        for key in possible_answer_dict:
            for ans in possible_answer_dict[key]:
                if ans in text.lower():
                    # found a match, returning
                    return key
        # if reached here, then no match was found
        print('NOT PARSED: ', text)
        return 'NOT ENOUGH INFO'
    
    def get_final_answer(self, model, data_point):
        print("****** Edited rationales: ", "First, " + data_point["edited_rationale_1"] + " Second, " + data_point["edited_rationale_2"])
        s3_answer_consolidation_prompt = self.get_s3_consolidation_prompt(self.get_question(data_point), data_point["edited_rationale_1"], data_point["edited_rationale_2"])
        print('Final answer consolidation prompt: ', s3_answer_consolidation_prompt)
        final_answer = call_openai_api(model, s3_answer_consolidation_prompt, max_tokens=256, temperature=0, n=1)[1].strip()
        data_point["final_answer"] = self.get_ans_text(final_answer)
        print("****** Final answer:", final_answer)
        print("****** Original answer:", data_point["cot_sc_answer"])
        print("****** Gold answer:", self.get_ground_truth(data_point))
        return data_point