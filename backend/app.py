from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-4o",
    input="Give me a one-sentence response as a customer support bot giving someone help with their lost package."
)

print(response.output_text)