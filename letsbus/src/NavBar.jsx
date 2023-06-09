import React from 'react';
import logo from './img/logo.png';

const Navbar = () => {
  return (
    <nav>
      <img src={logo} alt="Logo" style={{ width: '300px', height: '100px' }}/>
    </nav>
  );
};

export default Navbar;