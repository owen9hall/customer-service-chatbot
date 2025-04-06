import { createChatBotMessage } from 'react-chatbot-kit';
import '../styling/chatbot.css';
// Adapted from react-chatbot-kit library docs: https://fredrikoseberg.github.io/react-chatbot-kit-docs/docs/

const botName = 'BoxBot'; // name of chatbot

// configure some chatbot settings
const config = {
   initialMessages: [createChatBotMessage(`Hello, I'm ${botName}! How may I assist you today?`)], // default message that begins conversation
   botName: botName,
   customStyles: {
      botMessageBox: {
         backgroundColor: '#f09d51ff',
      },
      chatButton: {
         backgroundColor: '#E0DFD5',
      },
   },
};

export default config;