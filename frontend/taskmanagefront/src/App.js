
import axios from 'axios'
import { useEffect } from 'react';
import './App.css';

import Form from  './components/Form.js' ;
import Main from  './components/Main.js' ;

/*
function App() {
  return (<Register/>);
}

export default App;

*/

function App() { 

  const [authenticated, setAuthenticated] = useState(False);
  useEffect(
    () => {
      const authenticate = async () => {
      try{
      const Response = await axios.get('http://127.0.0.1:8000/api/whoamI/')
      setAuthenticated=True
}
catch(error)
 {setAuthenticated=False}
}
authenticate()

    }, []
  ) 
return (
  <div>
    <h1>Welcome to Your App</h1>
    {authenticated ?(<Main/> ) : (<Form/>)}
  </div>
);
}

export default App;