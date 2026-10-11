from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os
load_dotenv()

groq_api_key = os.getenv("Groq_API_Key")
if not groq_api_key:
    raise ValueError("Groq API key is not set")

client = Groq(api_key=groq_api_key)

model = "openai/gpt-oss-20b"
role = "user"
prompt = "Hello, do you love me?"
message={"role": role, "content": prompt}
message_system = {"role": "system", "content": "you are a my stirct manager and you are 18 years old"}

messages = [message_system,message]  

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1.0
)

print(response.choices[0].message.content)  