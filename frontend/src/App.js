import React from 'react';
import './App.css';
import Navbar from './components/Navbar/Navbar';
import { Link, BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AppContext } from './AppContext';
import Home from './pages/Home';
import About from './pages/About';
import Teams from './pages/Team';
import SignUp from './pages/Signup';


function App() {
  const [userinfo, setUserInfo] = React.useState();
  const [searchParams, setSearchParams] = React.useState();

  return (
    <AppContext.Provider value={{ userinfo, setUserInfo, searchParams, setSearchParams}}>
      <Router>
        <Navbar />
        <Routes>
        <Route path='/' element={<Home />} />
          <Route path='/home' element={<Home />} />
          <Route path='/about' element={<About />} />
          <Route path='/team' element={<Teams />} />
          <Route path='/signup' element={<SignUp />} />
          <Route path='/api' element={<Link to={{ pathname: 'https://www.themealdb.com/'}}/> }/>
        </Routes>
      </Router>
    </AppContext.Provider>
  );
}
  
export default App;