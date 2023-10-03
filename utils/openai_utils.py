import openai
import os

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
                    timeout=60,
                    request_timeout=60,
                )
                return [response, response["choices"][0]["message"]["content"]]
            else:
                raise Exception("Invalid model name")
        except Exception as e:
            print('Retry due to:', e)
            error_times += 1
            continue
        
    return None

