import os
from dotenv import load_dotenv
from pathlib import Path
import groq

load_dotenv()

groq_api_key = os.getenv("Groq_API_Key")
if not groq_api_key:
    raise ValueError("Groq API key is not set")

client = groq.Groq(api_key=groq_api_key)

model = "openai/gpt-oss-20b"
role = "user"
promt1="Hi"
promt2="How are you?"
promt3="explain  achine learning"

promt=[promt1,promt2,promt3]

for prompt in promt:
    message={"role": role, "content": prompt}
    messages = [message]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=1000
    )
    print(f"promt:{prompt} \n your token usage prompt: {response.usage.prompt_tokens} \n your token usage response: {response.usage.completion_tokens} \n your token usage total: {response.usage.total_tokens} \n reason: {response.choices[0].finish_reason}")


