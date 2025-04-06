import UserList from '../components/UserList';
import '../styling/App.css'
import '../styling/styles.css'

// Landing page for the application containing the user list to select a user
function App() {

  // render the user list
  return (
   <div className="app-container" >
      <UserList />
      <p>Select a user to test the chatbot with.</p>
   </div>
 );
}

export default App;
