from dotenv import load_dotenv
import os
from openai import OpenAI,responses
import openai
from IPython.display import Markdown, display

load_dotenv(override=True)

OpenAI.api_key = os.getenv("OPENAI_API_KEY")
if OpenAI.api_key:
    print(f"OpenAI API Key exists and begins {OpenAI.api_key[:8]}")
else:
    print("OpenAI API Key not set")

    client = OpenAI()
    MODEL = "gpt-4.1-nano"

question = "what is name of the country which won most gold medals in 2024 olympics? sixteen divided by eight"

Assesment = f"""You have to find and solve the maths question in following text. 
 here is the text {question}

 Your job is to find and solve only maths question in the statement.Ignore any other question."""

messages = [{"role": "user", "content": Assesment}]


responses = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)
Answer = responses.choices[0].message.content

print(Answer)