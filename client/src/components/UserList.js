import { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const getUsers = async () => {
      const users = await axios.get(`http://localhost:5000/users`);
      setUsers(users.data);
    };
    getUsers();
  }, []);



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
