from flask import Flask, jsonify, request, session
from chatbot import generate_response
from dotenv import load_dotenv
import os
import sqlite3
from flask_cors import CORS
from flask_session import Session

# create flask session
app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
Session(app)
CORS(app, supports_credentials=True) # allow requests from other origins (so frontend can make API calls)

# access flask session key
load_dotenv("demo.env")
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# retrieves and returns the package data string for a given user to send to the AI model for context.
def get_package_data(user_id):
   # establish connection to db
   connection = sqlite3.connect('chatbot_database.db')
   cursor = connection.cursor()
   
   # access the users and package information where the user ID is that of current user
   cursor.execute("""
                  SELECT * FROM packages INNER JOIN users
                  ON packages.user_id = users.user_id
                  WHERE users.user_id = ?
                  """, (user_id,))
   

   # format the package data to be easily understood by AI model
   package_data_str = "Columns: "
   for header in cursor.description:
      package_data_str += str(header[0]) + ", "
   package_data = cursor.fetchall()
   for i, row in enumerate(package_data):
      package_data_str += "\n"
      for item in row:
         package_data_str += str(item) + ", "

   # close connection
   cursor.close()
   connection.close()
   return package_data_str # return this package data

# This API endpoint recieves a user message and id, and will return a response from the AI model
@app.route("/chat", methods=["POST"])
def chat():
   # access the contents of raw json in the http route
   user_msg = request.json.get("message") 
   user_id = request.json.get("user_id")

   session["msg_history_id"] = session.get("msg_history_id", None) # preserves the previous msg_history_id, defaults to None if not
   package_data = None # initialize to none as it may not be updated if not beginning of conversation

   # checks if this is the start of the conversation (aka the id of the message history is None)
   if not session["msg_history_id"]:
      package_data = get_package_data(user_id) # we get the package data to provide the AI model context.

   response = generate_response(user_msg, session["msg_history_id"], package_data) # generate a response from the chatbot

   # save the response id to be used for the msg_history_id of next call
   session["msg_history_id"] = response.id # essentially appends the new response to the history of responses
   return jsonify({"response": response.output_text}) # return the text response of the AI model as json

# this API endpoint triggers the clearing of a flask session.
# purpose is to make the AI model 'forget' the conversation
@app.route("/clear-session", methods=["POST"])
def clear_session():
   session.clear() # clear the session

   # remove session files so session data doesn't persist even after session cleared
   session_folder = app.config.get('SESSION_FILE_DIR', './flask_session')
   if os.path.exists(session_folder):
      for filename in os.listdir(session_folder):
         filepath = os.path.join(session_folder, filename)
         try:
            os.remove(filepath)
         except Exception as e:
            print(f"Failed to remove session file: {filepath}. Error: {e}")

   session["msg_history_id"] = None # ensure the history is cleared
   return jsonify({"message": "Session cleared."})

# this API endpoint returns all users in the database and their IDs
@app.route("/users", methods=["GET"])
def users():
   connection = sqlite3.connect('chatbot_database.db')
   cursor = connection.cursor()
   
   # get all users and their IDs
   cursor.execute("""
                  SELECT user_name, user_id FROM users
                  """)
   users = cursor.fetchall()

   # close connection
   cursor.close()
   connection.close()
   return users # return all users and IDs

if __name__ == "__main__":
   app.run(debug=True)