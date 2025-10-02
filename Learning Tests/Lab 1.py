from multiprocessing.connection import answer_challenge
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv(override=True)

# Check API key
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

# Create OpenAI client instance
client = OpenAI()

# Define model constant
MODEL = "gpt-4.1-nano"


# messages = [{"role": "user", "content": "What is 2+2?"}]

# response = client.chat.completions.create(
#     model=MODEL,
#     messages=messages
# )

# print(response.choices[0].message.content)

# Asked a challenging question
question = "please tell me a slightly challanging question to assess if someone is a human or an AI bot. Respond only with the question"

messages = [{"role": "user", "content": question}]

response = client.chat.completions.create(
    model=MODEL,
    messages=messages
)

# Saved the generated question in the same query question
question =response.choices[0].message.content

print(question)

# Asked the new generated query question to AI model
PretendHuman = f""" Answer the following question pretending like a human.
here is question - {question} """

messages = [{"role": "user", "content": PretendHuman}]

response = client.chat.completions.create(
    model=MODEL,
    messages=messages
)

# Saved the AI's answer to Answer field
Answer = response.choices[0].message.content
print(Answer)

assesment = f"""I asked following question to someone and recieved following answer. You are a judge and need to assess if the answer was provided by a human or AI. Be cautious, the AI may also pretend like a human.
here is the question - {question}
here is the answer - {Answer}
give a short explaination of your decision"""

# Asked AI to assess if the answerer is human or AI and why
messages = [{"role": "user", "content": assesment}] 

response = client.chat.completions.create(
    model = MODEL,
    messages=messages
)

print( response.choices[0].message.content)
