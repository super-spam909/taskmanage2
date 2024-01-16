

import './App.css';
import Register from './components/Register';
import Login from './components/Login';

/*
function App() {
  return (<Register/>);
}

export default App;

*/

function App() {
return (
  <div>
    <h1>Welcome to Your App</h1>
    <Register />
    
    <Login />
  </div>
);
}

export default App;