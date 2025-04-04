from flask import Flask, jsonify, request, session
from chatbot import generate_response
from dotenv import load_dotenv
import os
import sqlite3
from flask_cors import CORS


app = Flask(__name__)
CORS(app) # allow requests from other origins

load_dotenv()
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.before_request
def clear_session_on_restart():
    session.clear()

def get_package_data(user_id):
   connection = sqlite3.connect('chatbot_database.db')
   cursor = connection.cursor()
   
   cursor.execute("""
                  SELECT * FROM packages INNER JOIN users
                  ON packages.user_id = users.user_id
                  WHERE users.user_id = ?
                  """, (user_id,))
   
   package_data_str = "Columns: "
   for header in cursor.description:
      package_data_str += str(header[0])
   package_data = cursor.fetchall()
   for i, row in enumerate(package_data):
      package_data_str += "\n"
      for item in row:
         package_data_str += str(item) + ", "

   cursor.close()
   connection.close()
   return package_data_str

# Chat API Route
@app.route("/chat", methods=["POST"])
def chat():
   user_msg = request.json.get("message")
   user_id = request.json.get("user_id")

   # clears conversation history if the user says 'reset'
   if user_msg.lower() == "reset":
      session.clear()

   msg_history_id = session.get("msg_history_id", None) # preserves the previous msg_history_id, defaults to None if not
   package_data = None
   if not msg_history_id:
      package_data = get_package_data(user_id)
      print(f"Package type: {type(package_data)}")
      print(f"Package data: {package_data}")

   # generate a response from the chatbot
   response = generate_response(user_msg, msg_history_id,package_data)

   # save the response id to be used for the msg_history_id of next call
   session["msg_history_id"] = response.id
   return jsonify({"response": response.output_text}) # return the text response of the bot as json

if __name__ == "__main__":
   app.run(debug=True)