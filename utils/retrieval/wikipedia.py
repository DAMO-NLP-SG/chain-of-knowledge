import json
from serpapi import GoogleSearch
import pickle
from tqdm.notebook import tqdm
import os.path
import os
import openai
from datasets import load_dataset
from transformers import DPRQuestionEncoder, DPRQuestionEncoderTokenizer

verify_question_demonstration = """
Write a question that asks about the answer to the overall question.

Overall Question: The Sentinelese language is the language of people of one of which Islands in the Bay of Bengal?
Answer: The language of the people of North Sen- tinel Island is Sentinelese.
Question: What peoples ́ language is Sentinelese?

Overall Question: Two positions were filled in The Voice of Ireland b which British-Irish girl group based in London, England?
Answer: Little Mix is based in London, England. 
Question: What girl group is based in London, England?

Overall Question: Where were the Olympics held when the 1993 World Champion figure skater's home country won it's second Winter Games gold medal?
Answer: the 1993 World Champion figure skater's home country is Canada.
Question: What is the home country of the 1993 World Champion figure skater?
"""

def call_openai_api(model, input_text, max_tokens=256, temperature=0, n=1):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    error_times = 0
    
    while error_times < 5:
        try:
            if "text-davinci" in model:
                # InstructGPT models, text completion
                response = openai.Completion.create(
                    model=model,
                    prompt=input_text,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    n=n,
                )
                return [response, response["choices"][0]["text"]]
            elif "gpt-" in model:
                # ChatGPT models, chat completion
                response = openai.ChatCompletion.create(
                    model=model,
                    messages = [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": input_text}
                    ],
                    max_tokens=max_tokens,
                    temperature=temperature,
                    n=n,
                )
                return [response, response["choices"][0]["message"]["content"]]
            else:
                raise Exception("Invalid model name")
        except Exception as e:
            print('Retry due to:', e)
            error_times += 1
            continue
        
    return None


def generate_wikipedia_query(input, overall_question):
    prompt = verify_question_demonstration + "\nOverall Question: " + overall_question + \
            "\nAnswer: " + input + "\nQuestion: "
            
    query = call_openai_api("text-davinci-003", prompt, max_tokens=256, temperature=0, n=1)[1].strip()
    query += " @wikipedia"
    return query

def execute_wikipedia_query(query):
    key = os.environ.get("SERPAPI_KEY")
    params = {
        "engine": "google",
        "q": query,
        "api_key": key,
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    # if "error" in results:
    #     raise Exception(results["error"])

    knowl = ""

    if "answer_box" in results:
        if "snippet" in results["answer_box"]:
            knowl += results["answer_box"]["snippet"]
            knowl += " "
        
    # organic answers
    if "organic_results" in results:
        # yield maximun 3 snippets
        if len(knowl) == 0:
            # if no answer box, yield maximun 3 snippets
            num_snippets = min(3, len(results["organic_results"]))
        else:
            num_snippets = min(2, len(results["organic_results"]))
            
        for i in range(num_snippets):
            if "snippet" in results["organic_results"][i]:
                knowl += results["organic_results"][i]["snippet"]
                knowl += " "
    return knowl


def retrieve_wikipedia_knowledge(input, data_point):
    print("Generate query...")
    query = generate_wikipedia_query(input, data_point["question"])
    print(query)
    print("Retrieve knowledge...")
    knowl = execute_wikipedia_query(query)
    print(knowl)
    return knowl
