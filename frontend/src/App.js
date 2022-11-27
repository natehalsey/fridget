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
import UserRecipes from "./components/UserRecipes";


function App() {
  const [user, setUser] = React.useState({});
  const [searchParams, setSearchParams] = React.useState("name");

  return (
    <AppContext.Provider value={{ user, setUser, searchParams, setSearchParams}}>
      <ThemeProvider theme={theme}>
        <Router>
          <Navbar />
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path={routes.home} element={<Home />} />
            <Route path={routes.about} element={<About />} />
            <Route path={routes.myrecipes} element={<UserRecipes />}/>
            <Route path='/recipe/:id' element={<RecipeView />} />
            <Route path='/create' element={<About />} />
            <Route path='/fridget' element={<About />} />
          </Routes>
        </Router>
      </ThemeProvider>
    </AppContext.Provider>
  );
}
  
export default App;