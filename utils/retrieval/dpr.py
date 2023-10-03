# dpr
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


def generate_dpr_query(input, overall_question):
    prompt = verify_question_demonstration + "\nOverall Question: " + overall_question + \
            "\nAnswer: " + input + "\nQuestion: "
            
    query = call_openai_api("text-davinci-003", prompt, max_tokens=256, temperature=0, n=1)[1].strip()
    return query


def execute_dpr_query(query):
    wiki_dataset = load_dataset("wiki_dpr", "psgs_w100.multiset.compressed", split="train")
    
    tokenizer = DPRQuestionEncoderTokenizer.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
    model = DPRQuestionEncoder.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
    question = query
    question_embedding = model(**tokenizer(question, return_tensors="pt"))[0][0].detach().numpy()

    scores, retrieved_Examples = wiki_dataset.get_nearest_examples("embeddings", question_embedding, k=1)
    knowl = retrieved_Examples["text"][0]
    return knowl


def retrieve_dpr_knowledge(input, data_point):
    print("Generate query...")
    query = generate_dpr_query(input, data_point["question"])
    print(query)
    print("Retrieve knowledge...")
    knowl = execute_dpr_query(query)
    print(knowl)
    return knowl