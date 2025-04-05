import { createChatBotMessage } from 'react-chatbot-kit';
import '../styling/chatbot.css';

const botName = 'BoxBot';

const config = {
   initialMessages: [createChatBotMessage(`Hello, I'm ${botName}! How may I assist you today?`)],
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