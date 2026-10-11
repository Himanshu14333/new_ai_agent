import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("Groq_API_Key")

if not groq_api_key:
    raise ValueError("Groq API key is not set")

client = Groq(api_key=groq_api_key)

# llama-3.3-70b-versatile was retired for free/developer Groq keys
model = "openai/gpt-oss-20b"
role = "user"
prompt = "Hello, who is messi?"
message={"role": role, "content": prompt}
messages = [message]

response = client.chat.completions.create(
    model=model,
    messages=messages,
)


print(response.choices[0].message.content)