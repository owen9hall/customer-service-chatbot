import './App.css';
import Chatbot from 'react-chatbot-kit'
import 'react-chatbot-kit/build/main.css'

import config from "./chatbot/chatbotConfig";
import MessageParser from "./chatbot/MessageParser";
import ActionProvider from "./chatbot/ActionProvider";

function App() {
  return (
    <>
      <Chatbot
        config={config}
        messageParser={MessageParser}
        actionProvider={ActionProvider}
        headerText='Chatbot'
        placeholderText='Input placeholder'
      />
    </>
  );
}

export default App;
