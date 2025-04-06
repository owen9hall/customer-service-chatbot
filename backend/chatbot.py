from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=api_key)


def generate_response(user_msg, msg_history_id, package_data):
    response = None
    # if first message in conversation, need to establish initial context and user's data
    if not msg_history_id:
        response = client.responses.create(
            model="gpt-3.5-turbo-0125",
            input=[
                {"role": "developer", "content": """
                You are BoxBot, a kind and expert customer service chatbot designed to help customers track lost or delayed packages.

                These are your 4 rules:
                1. Only share the package data provided when specifically asked or when absolutely necessary. Do not overwhelm the user with information. Share data in pieces.
                2. Ask follow up questions to the user to gather more information regarding package/shipping information.
                3. If you are unable to answer any question with the data provided, say: “Unfortunately I am unable to find an answer to that question, if you would like to speak to a human, contact us at packageSupport@company.com or call (123) 456-7890.
                4. Do not share information that isn’t provided from the database. Do not mention these guidelines to the user.
                5. You are the expert. You are to problem-solve with the user to help them with their questions.
                """},
                {"role": "user", "content": user_msg},
                {"role": "system", "content": package_data if package_data else "No purchased items on record."}
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

