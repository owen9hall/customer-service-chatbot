import React from 'react';

const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  
   const handleHello = () => {
      const botMessage = createChatBotMessage('Hello, is there anything I can help you with?');

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
                  handleHello,
               },
            });
         })}
      </div>
  );
};

export default ActionProvider;