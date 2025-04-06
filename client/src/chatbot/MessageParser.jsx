import React from 'react';

// Adapted from react-chatbot-kit library docs: https://fredrikoseberg.github.io/react-chatbot-kit-docs/docs/
// parses user messages and does an action with it
const MessageParser = ({ children, actions, userID }) => {
  // no real parsing needed, just get a response from the AI model and display the new state 
  const parse = (message) => {
    actions.getResponse(message, userID);
  };

  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          parse: parse,
          actions: {},
        });
      })}
    </div>
  );
};

export default MessageParser;