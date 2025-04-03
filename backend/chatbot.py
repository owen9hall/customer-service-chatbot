from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=api_key)


def generate_response(user_msg, msg_history_id):
    response = None
    if msg_history_id is None: # first message in conversation, so developer instructions need to be established
        response = client.responses.create(
            model="gpt-3.5-turbo-0125",
            input=[
                {"role": "developer", "content": "You are a customer service chatbot helping customers track lost packages. You are kind and professional."},
                {"role": "user", "content": user_msg}
            ]
        )
    else:
        response = client.responses.create(
            model="gpt-3.5-turbo-0125",
            previous_response_id=msg_history_id,
            input=[{"role": "user", "content": user_msg}],
        )
    print(response.output_text)
    return response

