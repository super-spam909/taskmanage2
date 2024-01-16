import React, {useState} from 'react'
import axios from 'axios' 


export default function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const [message, setMessage] = useState('')

    const handleLogin =async(event) => {
      event.preventDefault();
      try{

      const Response = await axios.post('http://127.0.0.1:8000/api/login/',
      { "username" : username,
      "password": password,})

      setMessage(Response.data['message'])
    } catch(error) {
      setMessage("User already exists: Try registering")
    }
    }

    
  return (
    <div>
<form onSubmit={handleLogin} >
    <label >Username:</label>
    <input type="text" id="username"  required onChange={(e)=> setUsername(e.target.value)} />

    <label >Password:</label>
    <input type="password" id="password"  required onChange={(e)=> setPassword(e.target.value)} />

    <button type = "submit" >Login</button>
</form>
<p>{message}</p>
</div>
  )
}