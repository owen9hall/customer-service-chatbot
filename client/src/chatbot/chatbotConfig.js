import { createChatBotMessage } from 'react-chatbot-kit';

const botName = 'PackagePal';

const config = {
   initialMessages: [createChatBotMessage(`Hello, I'm ${botName}! How may I assist you today?`)],
   botName: botName,
   customStyles: {
      botMessageBox: {
         backgroundColor: '#a8bdad',
      },
      chatButton: {
         backgroundColor: '#78adcf',
      },
   },
};

export default config;