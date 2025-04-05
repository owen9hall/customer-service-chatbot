import './styling/App.css';
import 'react-chatbot-kit/build/main.css'

import Home from "./pages/Home";
import { useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.css'
import './styling/styles.css'

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
      <Home />
    </>
  );
}

export default App;
