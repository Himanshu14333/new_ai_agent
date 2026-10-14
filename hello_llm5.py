import os
from pathlib import Path
from time import sleep
from dotenv import load_dotenv
from groq import Groq
import re

load_dotenv()
my_api_key=os.getenv("Groq_API_Key")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
model="openai/gpt-oss-20b"

def get_product_price(product):
    if product == 'iPhone 17':
        return 1000
    elif product == "iPhone 15":
        return 500
    else:
        return 0
    
def calculator(expression):
    try:
        return eval(expression)
    except:
        return "calc error!"

tools = {
    "get_product_price": get_product_price,
    "calculator": calculator
}
system_prompt = """
"""

def run_agent(question):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(5):

        print("\n------------------")
        print("STEP", step + 1)
        print("------------------")

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0
        )

        answer = response.choices[0].message.content

        print(answer)

        # Agent has finished
        if "Final Answer:" in answer:
            break


        # Find the Action
        match = re.search(
            r"Action:\s*(\w+)\((.*?)\)",
            answer
        )


        if match:

            tool_name = match.group(1)

            tool_input = match.group(2)

            tool_input = tool_input.strip()

            tool_input = tool_input.strip('"')


            # Run the tool
            if tool_name in tools:

                tool = tools[tool_name]

                observation = tool(tool_input)

            else:

                observation = "Tool not found"


            print(
                "Observation:",
                observation
            )


            # Add LLM response to memory
            messages.append({
                "role": "assistant",
                "content": answer
            })


            # Give tool result back to LLM
            messages.append({
                "role": "user",
                "content":
                    "Observation: "
                    + str(observation)
            })
            sleep(5)



prompt="""
I have 5000 rupees. What is the price of an iphone 17?
and how much money will I have left?
"""
run_agent(prompt)