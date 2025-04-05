from flask import Flask, jsonify, request, session
from chatbot import generate_response
from dotenv import load_dotenv
import os
import sqlite3
from flask_cors import CORS
from flask_session import Session
import shutil


app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
Session(app)
CORS(app, supports_credentials=True) # allow requests from other origins

load_dotenv()
app.secret_key = os.getenv("FLASK_SECRET_KEY")

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
      package_data_str += str(header[0]) + ", "
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
   session["msg_history_id"] = session.get("msg_history_id", None) # preserves the previous msg_history_id, defaults to None if not
   package_data = None
   if not session["msg_history_id"]:
      session["msg_history_id"] = None
      package_data = get_package_data(user_id)
      print(f"Package data: {package_data}")

   # generate a response from the chatbot
   response = generate_response(user_msg, session["msg_history_id"], package_data)

   # save the response id to be used for the msg_history_id of next call
   session["msg_history_id"] = response.id
   return jsonify({"response": response.output_text}) # return the text response of the bot as json

@app.route("/clear-session", methods=["POST"])
def clear_session():
   session.clear()

   # removes session files so session data doesn't persist even after session cleared
   session_folder = app.config.get('SESSION_FILE_DIR', './flask_session')
   if os.path.exists(session_folder):
      for filename in os.listdir(session_folder):
         filepath = os.path.join(session_folder, filename)
         try:
            os.remove(filepath)
         except Exception as e:
            print(f"Failed to remove session file: {filepath}. Error: {e}")

   session["msg_history_id"] = None
   return jsonify({"message": "Session cleared."})

if __name__ == "__main__":
   app.run(debug=True)