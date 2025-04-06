import '../styling/Home.css';
import Chatbot from 'react-chatbot-kit'
import 'react-chatbot-kit/build/main.css'
import config from "../chatbot/chatbotConfig";
import MessageParser from "../chatbot/MessageParser";
import ActionProvider from "../chatbot/ActionProvider";
import { useParams } from 'react-router-dom';
import { useEffect } from 'react';
import axios from 'axios';

function Home() {
   const { userID } = useParams();

   // clears flask session on page render, effectively making the chatbot forget conversation history
   useEffect(() => {
      const clearSession = async () => {
        await axios.post('http://localhost:5000/clear-session');
      };

      clearSession();
    }, []);

   return (
      <div className="home-container" >
         <Chatbot
            config={config}
            messageParser={(props) => MessageParser({ ...props, userID })}
            actionProvider={ActionProvider}
            headerText='BoxBot'
            placeholderText='Write a message...'
         />
      </div>
   );
}

export default Home;