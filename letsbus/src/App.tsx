import React from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import './App.css';
import './button.css';
import background from "./img/background.png";
import Navbar from './NavBar';
import logo from './img/logo.png';




function App() {
  return (
    <div className="App">
      <div className="container" style={{ backgroundImage:`url(${background})`}}>
      <main className="content">
      <div className='logo'>
      <img src={logo} alt="Logo" style={{ width: '300px', height: '100px' }}/>
      </div>
      <div className='buttonsDiv'>
      <button className='button'>הוספת דיווח</button>
      <br></br>
      <br></br>
      <button className='button'>קבלת מידע</button>
      </div>
      </main>
    </div>
    </div>
  );
}

export default App;
