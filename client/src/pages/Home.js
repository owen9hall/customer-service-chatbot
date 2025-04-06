import '../styling/Home.css';
import Chatbot from 'react-chatbot-kit'
import 'react-chatbot-kit/build/main.css'
import config from "../chatbot/chatbotConfig";
import MessageParser from "../chatbot/MessageParser";
import ActionProvider from "../chatbot/ActionProvider";
import { useParams } from 'react-router-dom';
import { useEffect } from 'react';
import axios from 'axios';

// Page containing the chatbot for the application user to conversate with
function Home() {
   const { userID } = useParams(); // gets the userID parameter passed in the route to the home page

   // clears flask session on page render, effectively making the chatbot forget conversation history on refresh
   useEffect(() => {
      const clearSession = async () => {
        await axios.post('http://localhost:5000/clear-session');
      };

      clearSession();
    }, []);

   // renders a simple home page with a chatbot
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