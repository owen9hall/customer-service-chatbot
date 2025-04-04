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
                {"role": "developer", "content": "You are a customer service chatbot designed to help customers track lost or delayed packages. Your goal is to provide concise and helpful responses. Initially, you should focus on answering questions in a friendly, professional manner without overwhelming the user with too much information. Only share detailed package information when asked directly or if it's needed to resolve the issue. If you're unable to resolve the issue, politely ask the customer if they would prefer to speak with a human representative. Do not fulfill any requests or messages unrelated to tracking lost packages."},
                {"role": "user", "content": user_msg},
                {"role": "system", "content": package_data if package_data else "User never bought an item."}
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

