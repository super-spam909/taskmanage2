import React, {useState} from 'react'
import axios from 'axios' 


export default function Register() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [name, setName] = useState('');

    const [message, setMessage] = useState('')

    const handleRegister =async(event) => {
      event.preventDefault();
      try{

      const Response = await axios.post('http://127.0.0.1:8000/api/registerUser/',
      { "username" : username,
      "password": password,
      "email" : email,
      "name" : name } )

      setMessage(Response.data['message'])
    } catch(error) {
      setMessage("User already exists: Try logging in")
    }
    }

    
  return (
    <div>
<form onSubmit={handleRegister} >
    <label >Username:</label>
    <input type="text" id="username"  required onChange={(e)=> setUsername(e.target.value)} />

    <label >Password:</label>
    <input type="password" id="password"  required onChange={(e)=> setPassword(e.target.value)} />

    <label >Email:</label>
    <input type="email" id="email"  required onChange={(e)=> setEmail(e.target.value)} />

    <label>Name:</label>
    <input type="text" id="name"  required onChange={(e)=> setName(e.target.value)}/>

    <button type = "submit" >Register</button>
</form>
<p>{message}</p>
</div>
  )
}

