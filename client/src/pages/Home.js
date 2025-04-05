import '../styling/Home.css';
import Chatbot from 'react-chatbot-kit'
import 'react-chatbot-kit/build/main.css'

import config from "../chatbot/chatbotConfig";
import MessageParser from "../chatbot/MessageParser";
import ActionProvider from "../chatbot/ActionProvider";

function Home() {
   return (
      <div className="home-container" >
         <Chatbot
            config={config}
            messageParser={MessageParser}
            actionProvider={ActionProvider}
            headerText='BoxBot'
            placeholderText='Write a message...'
         />
      </div>
   );
}

export default Home;