import React from "react";
import "./App.css";
import Navbar from "./components/Navbar";
import { Link, BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppContext, theme, routes } from "./constants";
import Home from "./pages/Home";
import About from "./pages/About";
import SignUp from "./pages/Signup";
import RecipeView from "./components/RecipeView";
import { ThemeProvider, styled } from "@mui/material/styles";
import Login from "./pages/Login";
import axios from "axios";
import MyRecipes from "./pages/MyRecipes";
import MyFridget from "./pages/MyFridget";
import MenuTray from "./components/MenuTray";
import { Box } from "@mui/material";
import Create from "./pages/Create";

axios.defaults.withCredentials = true;

/**
 * The App function is the main function of the application. It is the parent of all other components.
 * It is responsible for setting the state of the application, and passing that state down to the
 * children components
 * @returns The App component is being returned.
 */
function App() {
  const [saved, setSaved] = React.useState({});
  const [searchParams, setSearchParams] = React.useState("name");
  const [showMenu, setShowMenu] = React.useState(false);
  const [menuItems, setMenuItems] = React.useState([]);
  const [checked, setChecked] = React.useState([]);

  if (localStorage.getItem("auth") === null) {
    localStorage.setItem("auth", false);
  }

  window.addEventListener("resize", (event) => {
    setShowMenu(false);
  });

  return (
    <AppContext.Provider
      value={{
        menuItems,
        setMenuItems,
        showMenu,
        setShowMenu,
        saved,
        setSaved,
        searchParams,
        setSearchParams,
        checked,
        setChecked,
      }}
    >
      <ThemeProvider theme={theme}>
        <Router>
          <Navbar />
          <Box className="traycontainer">
            <MenuTray className="tray" />
          </Box>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path={routes.home} element={<Home />} />
            <Route path={routes.about} element={<About />} />
            <Route path={routes.myrecipes} element={<MyRecipes />} />
            <Route path="/recipe/:id" element={<RecipeView />} />
            <Route path="/fridget" element={<MyFridget />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path={routes.create} element={<Create />} />
          </Routes>
        </Router>
      </ThemeProvider>
    </AppContext.Provider>
  );
}

export default App;
