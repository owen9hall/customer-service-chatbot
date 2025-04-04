import React from 'react';

const MessageParser = ({ children, actions }) => {
  const parse = (message) => {
      actions.getResponse(message, 1);
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