import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { Link, BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AppContext, theme, routes } from './constants';
import Home from './pages/Home';
import About from './pages/About';
import SignUp from './pages/Signup';
import RecipeView from './components/RecipeView';
import { ThemeProvider, styled } from '@mui/material/styles';
import Login from './pages/Login';
import axios from 'axios'
import MyRecipes from './pages/MyRecipes';

axios.defaults.withCredentials = true

function App() {
  const [saved, setSaved] = React.useState({})
  const [searchParams, setSearchParams] = React.useState("name");

  return (
    <AppContext.Provider value={{ saved, setSaved, searchParams, setSearchParams}}>
      <ThemeProvider theme={theme}>
        <Router>
          <Navbar />
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path={routes.home} element={<Home />} />
            <Route path={routes.about} element={<About />} />
            <Route path={routes.myrecipes} element={<MyRecipes />}/>
            <Route path='/recipe/:id' element={<RecipeView />} />
            <Route path='/create' element={<About />} />
            <Route path='/fridget' element={<About />} />
            <Route path='/login' element={<Login/>} />
            <Route path='/signup' element={<SignUp/>} />
          </Routes>
        </Router>
      </ThemeProvider>
    </AppContext.Provider>
  );
}
  
export default App;