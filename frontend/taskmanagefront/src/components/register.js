import React from 'react'

export default function register() {
    const handleRegister =async(event) => {

    }
  return (
<form onSubmit={handleRegister} >
    <label ="username">Username:</label>
    <input type="text" id="username" name="username" required />

    <label ="password">Password:</label>
    <input type="password" id="password" name="password" required />

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required />

    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required />

    <button type = "submit" >Register</button>
<form/>
  )
}
