import React from 'react';
import axios from 'axios';

// Adapted from react-chatbot-kit library docs: https://fredrikoseberg.github.io/react-chatbot-kit-docs/docs/
// executes chatbot actions such as fetching and creating a chatbot response.
const ActionProvider = ({ createChatBotMessage, setState, children }) => {

   // action to get a chatbot response
   const getResponse = async (userMessage, userID) => {
      // This is the default message the bot will display -- will be overridden unless bot encounters and error
      let botMessage = createChatBotMessage('I apologize, it seems I have encountered an error. If you would like to speak to a human agent please contact us at packageSupport@company.com or call (123)456-7890.');
      try {
         // prepare API POST request data & config
         const data = {
            message: userMessage,
            user_id: userID
         };
         const config = {
            headers: {
               'Content-Type': 'application/json'
            },
            withCredentials: true, // allows flask session to cache previous messages
         };

         const response = await axios.post(`http://localhost:5000/chat`, data, config); // make request for AI model to craft a response to the user message
         botMessage = createChatBotMessage(response.data.response); // set the chatbot message to be the AI model's response

      } catch (error) {
         console.error("Error fetching chatbot response: ", error);
      }
      // add new message to all previous messages to be displayed
      setState((prev) => ({
         ...prev,
         messages: [...prev.messages, botMessage],
      }));
   }

   return (
      <div>
         {React.Children.map(children, (child) => {
            return React.cloneElement(child, {
               actions: {
                  getResponse,
               },
            });
         })}
      </div>
   );
};

export default ActionProvider;