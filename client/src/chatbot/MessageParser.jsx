import React from 'react';

const MessageParser = ({ children, actions, userID }) => {
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