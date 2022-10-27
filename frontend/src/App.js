import React from 'react';
import './App.css';
import Navbar from './components/Navbar/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages';
import About from './pages/about';
import Teams from './pages/team';
import SignUp from './pages/signup';
  
function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path='/' exact component={Home} />
        <Route path='/about' component={About} />
        <Route path='/team' component={Teams} />
        <Route path='/sign-up' component={SignUp} />
      </Routes>
    </Router>
  );
}
  
export default App;