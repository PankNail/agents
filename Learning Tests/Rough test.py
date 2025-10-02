from dotenv import load_dotenv
import os
from openai import OpenAI, responses
import openai

from IPython.display import Markdown, display

load_dotenv(override=True)

openai.api_key = os.getenv("OPENAI_API_KEY")
if openai.api_key:
    print(f"OpenAI API Key exists and begins {openai.api_key[:8]}")
else:
    print("OpenAI API Key not set")

    openai = OpenAI()
    # Define model constant
    MODEL = "gpt-4.1-nano"

# messages = [{"role": "user", "content": "What is 2+2?"}]

# responses = openai.chat.completions.create(
#     model=model,
#     messages=messages
# )

# print(responses.choices[0].message.content)

question = "how simple agentic systems can be to reduce carbon footprint of a business. Answer with some examples"
messages = [{"role": "user", "content": question}]

responses = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

Answer = responses.choices[0].message.content

print(Answer)

display(Markdown(Answer))

Assesment = f"""You are to rank the examples in following article. 
here is the article {Answer}

Your job is to rank the example based on practical feasiblities, potential challenges and easy monetization. Include a summary for reason for ranking."""

message = [{"role": "user", "content": Assesment}]
responses = openai.chat.completions.create(model="gpt-4.1-nano",messages=message) 

print(responses.choices[0].message.content)



