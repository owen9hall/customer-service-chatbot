import React from 'react';
import axios from 'axios';

const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  
   const handleHello = () => {
      const botMessage = createChatBotMessage('Hello, is there anything I can help you with?');

      setState((prev) => ({
         ...prev,
         messages: [...prev.messages, botMessage],
      }));
   }

   const getResponse = async (userMessage, userID) => {
      // default message if not overridden
      let botMessage = createChatBotMessage('It seems I have encountered an error.');
      try {
         const data = {
            message: userMessage,
            user_id: userID
         };
         const config = {
            headers: {
               'Content-Type': 'application/json'
            }
         };
         const response = await axios.post(`http://localhost:5000/chat`, data, config);
         botMessage = createChatBotMessage(response.data.response);

      } catch (error) {
         console.error("Error fetching chatbot response: ", error);
      }

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