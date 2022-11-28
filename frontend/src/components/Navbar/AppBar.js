import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import AdbIcon from '@mui/icons-material/Adb';
import { AppContext, logoutURL, routes } from "../../constants";
import { useNavigate } from "react-router-dom";
import { Icon } from '@iconify/react';
import axios from 'axios';
import { API_URL  } from '../../constants';

const navbarElements = [
  {
    key: 0,
    name: "Search",
    link: "/home",
    hide: 1
  },
  {
    key: 1,
    name: "My Recipes",
    link: "/about",
    hide: 0
  },
  {
    key: 2,
    name: "About",
    link: "/about",
    hide: 1
  },
];

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
    axios.post(
      API_URL + logoutURL
    ).then( (response) => {
        navigate(routes.home); 
    })
    .catch( (error) => {
      console.log(error);
    });
    return 

  };

  return (
    <AppBar position="static">
      <Container maxWidth="xl">

        {/* placeholder */}
        <Toolbar disableGutters>
          <Icon icon="mdi:fridge" href="/" style={{ fontSize: '36px' }}/>
          <Typography
            variant="h6"
            noWrap
            component="a"
            href="/"
            sx={{
              mr: 2,
              display: { xs: 'none', md: 'flex' },
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            Fridget
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
              <MenuItem
                key={0}
                onClick={() => navigate(`/home`)}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                Search
              </MenuItem>
              <MenuItem
                key={2}
                onClick={() => navigate(`/about`)}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                About
              </MenuItem>

          </Box>
          {localStorage.getItem("auth") === "true" && <MenuItem
                key={1}
                onClick={() => navigate( `/myrecipes`)}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                <Typography textAlign="center">My Recipes</Typography>
              </MenuItem>
          }
          {localStorage.getItem("auth") === "true" && <MenuItem key={3} onClick={handleLogout}>
              <Typography textAlign="center">Log Out</Typography>
            </MenuItem>
          }

          {localStorage.getItem("auth") === "false" && <MenuItem key={1} onClick={() => navigate(routes.login)}>
              <Typography textAlign="center">Sign Up</Typography>
            </MenuItem>
          }
          {localStorage.getItem("auth") === "false" && <MenuItem key={2} onClick={() => navigate(routes.login)}>
              <Typography textAlign="center">Log In</Typography>
            </MenuItem>
          }

        </Toolbar>
      </Container>
    </AppBar>
  );
}
export default ResponsiveAppBar;
