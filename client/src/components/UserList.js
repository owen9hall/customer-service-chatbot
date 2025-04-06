import { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

// Component to render a list of all users in the database. Selecting an option routes the application user to a chatbot conversation with the specific person selected.
function UserList() {
  const [users, setUsers] = useState([]); // create a useState variable that contains a list of all usernames and userIDs

  // make a get request to fetch a list of all usernames and userIDs when the page is first rendered
  useEffect(() => {
    const getUsers = async () => {
      const users = await axios.get(`http://localhost:5000/users`);
      setUsers(users.data); // update the user useState variable to the response of the call
    };
    getUsers();
  }, []);



  // render a list of users and route the application user to the home page (containing the chatbot) while passing the userID in the route
  return (
    <>
      <h2>Select user:</h2>
      <ul className="list-group">
        {users.map((user) => (
          <li 
            key={user[1]}>
            <Link to={`/home/${user[1]}`}>
              <h5>{user[0]}</h5>
            </Link>
          </li>
        ))}
      </ul>
    </>
  );
}

export default UserList;
