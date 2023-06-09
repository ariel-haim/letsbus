import React, { useState }  from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import './App.css';
import './button.css';
import './input_box.css';
import background from "./img/background.png";
import Navbar from './NavBar';
import { sys } from 'typescript';




function App() {
  const [showButton1, setShowButton1] = useState(true);
  const [showButton2, setShowButton2] = useState(true);
  const [showTextBox1, setShowTextBox1] = useState(false);
  const [showTextBox2, setShowTextBox2] = useState(false);
  const [showButton3, setShowButton3] = useState(false);


  const handleButtonClick = (buttonNumber: any) => {
    if (buttonNumber === 1) {
      setShowButton1(false);
      setShowButton2(false);
      setShowTextBox1(true);
      setShowTextBox2(true);
      setShowButton3(true);
    }
  };
  return (
    <div className="App">
      <div className="container" style={{ backgroundImage:`url(${background})`}}>
      <main className="content">
      <Navbar></Navbar>
      <div className='buttonsDiv'>
      {showButton1 && (
        <button className='button' onClick={() => handleButtonClick(1)}>הוספת דיווח</button>
      )}
      <br></br>
      <br></br>
      {showButton2 && (
        <button className='button' onClick={() => handleButtonClick(1)}>קבלת מידע</button>
      )}
      {showTextBox1 && <input type="text" name="name" className="question" id="nme" placeholder='מה מספר הקו?'/>}
      <br></br>
      {showTextBox2 && <input type="text" name="name" className="question" id="nme" placeholder='מה מספר התחנה?'/>}
      <br></br>
      {showButton3 && (
        <button className='button' onClick={() => handleButtonClick(2)}>!דווח</button>
      )}
      </div>
      </main>
    </div>
    </div>
  );
}

export default App;
