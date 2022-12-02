import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Menu from "@mui/material/Menu";
import DropDownMenu from "../DropDownMenu";
import MenuIcon from "@mui/icons-material/Menu";
import Container from "@mui/material/Container";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import Tooltip from "@mui/material/Tooltip";
import MenuItem from "@mui/material/MenuItem";
import AdbIcon from "@mui/icons-material/Adb";
import { AppContext, logoutURL, routes } from "../../constants";
import { useNavigate } from "react-router-dom";
import { Icon } from "@iconify/react";
import axios from "axios";
import { API_URL } from "../../constants";


/**
 * This function renders the app bar at the top of the page. It has a dropdown menu for mobile devices
 * and a menu for desktop devices. The menu items are different depending on whether the user is logged
 * in or not.
 */
function ResponsiveAppBar() {
  const [anchorElNav, setAnchorElNav] = React.useState(null);
  let navigate = useNavigate();

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleLogout = () => {
    localStorage.setItem("auth", false);
    axios
      .post(API_URL + logoutURL)
      .then((response) => {
        navigate(routes.home);
      })
      .catch((error) => {
        console.log(error);
      });
    return;
  };

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        {/* placeholder */}
        <Toolbar disableGutters>
          <Icon icon="mdi:fridge" href="/" style={{ fontSize: "36px" }} />
          <Box sx={{ flexGrow: 1, display: { xs: 1, md: "flex" } }}>
            <Typography
              variant="h6"
              noWrap
              component="a"
              href="/"
              sx={{
                mr: 2,
                display: { xs: 1, md: "flex" },
                fontFamily: "monospace",
                fontWeight: 700,
                letterSpacing: ".3rem",
                color: "inherit",
                textDecoration: "none",
              }}
            >
              Fridget
            </Typography>
          </Box>
          {localStorage.getItem("auth") === "false" ? (
            <Box
              className="dropdownbox"
              sx={{ flexGrow: 0, display: { xs: 1, md: "none" } }}
            >
              <DropDownMenu
                menu_items={[
                  { item: "Register", click: routes.signup },
                  { item: "Log In", click: routes.login },
                ]}
              />
            </Box>
          ) : (
            <Box
              className="dropdownbox"
              sx={{ flexGrow: 0, display: { xs: 1, md: "none" } }}
            >
              <DropDownMenu
                menu_items={[
                  { item: "Create Recipe", click: "/create" },
                  { item: "My Recipes", click: "/myrecipes" },
                  { item: "My Fridget", click: "/fridget" },
                  { item: "Log Out", click: null },
                ]}
              />
            </Box>
          )}
          <Box sx={{ flexGrow: 0, display: { xs: "none", md: "flex" } }}>
            <MenuItem
              key={0}
              onClick={() => navigate(`/home`)}
              sx={{ my: 2, color: "white", display: "block" }}
            >
              Search
            </MenuItem>
          </Box>
          {localStorage.getItem("auth") === "true" && (
            <Box sx={{ flexGrow: 0, display: { xs: "none", md: "flex" } }}>
              <MenuItem
                key={2}
                onClick={() => navigate(routes.myrecipes)}
                sx={{ my: 2, color: "white", display: "block" }}
              >
                My Recipes
              </MenuItem>
              <MenuItem key={4} onClick={() => navigate(`/fridget`)}>
                My Fridget
              </MenuItem>
              <MenuItem key={3} onClick={() => navigate(routes.create)}>
                Create Recipe
              </MenuItem>
              <MenuItem key={3} onClick={handleLogout}>
                Log Out
              </MenuItem>
            </Box>
          )}

          {localStorage.getItem("auth") === "false" && (
            <>
              <Box sx={{ flexGrow: 0, display: { xs: "none", md: "flex" } }}>
                <MenuItem
                  key={2}
                  onClick={() => navigate(routes.signup)}
                  sx={{ my: 2, color: "white", display: "block" }}
                >
                  Register
                </MenuItem>
                <MenuItem key={3} onClick={() => navigate(routes.login)}>
                  Log In
                </MenuItem>
              </Box>
            </>
          )}
        </Toolbar>
      </Container>
    </AppBar>
  );
}
export default ResponsiveAppBar;
