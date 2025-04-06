import UserList from '../components/UserList';
import '../styling/App.css'
import '../styling/styles.css'

function App() {
  return (
   <div className="app-container" >
      <UserList />
      <p>Select a user to test the chatbot with.</p>
   </div>
 );
}

export default App;
