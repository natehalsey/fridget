import React from 'react';
import './App.css';
import Navbar from './components/Navbar/Navbar';
import { Link, BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import Teams from './pages/Team';
import SignUp from './pages/SignUp';
  
function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path='/Home' element={<Home />} />
        <Route path='About' element={<About />} />
        <Route path='/Team' element={<Teams />} />
        <Route path='/Signup' element={<SignUp />} />
        <Route path='/Api' element={<Link to={{ pathname: 'https://www.themealdb.com/'}}/> }/>
      </Routes>
    </Router>
  );
}
  
export default App;