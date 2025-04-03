from flask import Flask, jsonify, request, session
from chatbot import generate_response
from dotenv import load_dotenv
import os


app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("FLASK_SECRET_KEY")

with app.app_context():
   session.clear()


# Chat API Route
@app.route("/chat", methods=["POST"])
def chat():
   user_msg = request.json.get("message")

   # clears conversation history if the user says 'reset'
   if user_msg.lower() == "reset":
      session.clear()

   msg_history_id = session.get("msg_history_id", None) # preserves the previous msg_history_id, defaults to None if not
   
   # generate a response from the chatbot
   response = generate_response(user_msg, msg_history_id)

   # save the response id to be used for the msg_history_id of next call
   session["msg_history_id"] = response.id
   return jsonify({"response": response.output_text}) # return the text response of the bot as json

if __name__ == "__main__":
   app.run(debug=True)