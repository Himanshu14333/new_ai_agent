import os
from dotenv import load_dotenv
import json
from pathlib import Path
from pydantic import BaseModel
import groq

load_dotenv()

groq_api_key = os.getenv("Groq_API_Key")
if not groq_api_key:
    raise ValueError("Groq API key is not set")

client = groq.Groq(api_key=groq_api_key)


class Person(BaseModel):
    name: str
    age: int
    city: str

schema = Person.model_json_schema() 



model = "openai/gpt-oss-20b"

response_format={
    "type": "json_object"
}

system_prompt = f"""extract the information strictly according to the schema and return it in json format: {schema}"""

system_message={"role": "system", "content": system_prompt}



role = "user"
text="hello, my name is John and I am 20 years old and I live in New York. i work for a company called Google and my job is to develop software for the company."
prompt = f"""extract the following information from the text: {text}"""
message={"role": role, "content": prompt}
messages = [system_message, message]

response = client.chat.completions.create(
    model=model,
    messages=messages, 
    response_format=response_format
)
print(response.choices[0].message.content)

