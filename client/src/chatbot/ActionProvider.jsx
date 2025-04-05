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
      let botMessage = createChatBotMessage('I apologize, it seems I have encountered an error. If you would like to speak to a human representative please contact us at packageCompany@company.com or call (123)456-7890.');
      try {
         const data = {
            message: userMessage,
            user_id: userID
         };
         const config = {
            headers: {
               'Content-Type': 'application/json'
            },
            withCredentials: true,
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