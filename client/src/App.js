import './App.css';
import Chatbot from 'react-chatbot-kit'
import 'react-chatbot-kit/build/main.css'

import config from "./chatbot/chatbotConfig";
import MessageParser from "./chatbot/MessageParser";
import ActionProvider from "./chatbot/ActionProvider";
import { useEffect } from 'react';
import axios from 'axios';

function App() {

    // clears flask session on page render, effectively making the chatbot forget conversation history
    useEffect(() => {
      const clearSession = async () => {
        await axios.post('http://localhost:5000/clear-session');
      };

      clearSession();
    }, []);


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
