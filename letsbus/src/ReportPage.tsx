import React from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import background from "./img/background.png";



function ReportPage() {
  return (
    <div className="App">
      <div className="container" style={{ backgroundImage:`url(${background})`}}>
      <main className="content">
        <h1>Report</h1>
      </main>
    </div>
    </div>
  );
}

export default ReportPage;
