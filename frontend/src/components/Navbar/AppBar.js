import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import AdbIcon from '@mui/icons-material/Adb';
import { AppContext, routes } from "../../constants";


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
  const {user} = React.useContext(AppContext)
  const [anchorElNav, setAnchorElNav] = React.useState(null);
  const [anchorElUser, setAnchorElUser] = React.useState(null);
  console.log(user);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  };
  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  return (
    <AppBar position="static">
      <Container maxWidth="xl">

        {/* placeholder */}
        <Toolbar disableGutters>
          <AdbIcon sx={{ display: { xs: 'none', md: 'flex' }, mr: 1 }} />
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
            LOGO
          </Typography>

          <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
              color="inherit"
            >
              <MenuIcon />
            </IconButton>
            <Menu
              id="menu-appbar"
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: 'bottom',
                horizontal: 'left',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'left',
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{
                display: { xs: 'block', md: 'none' },
              }}
            >
                <MenuItem key={1} onClick={() => {window.location.href = routes.home }}>
                  <Typography textAlign="center">Search</Typography>
                </MenuItem>
                {Object.keys(user).length > 0 && <MenuItem key={2} onClick={() => {window.location.href = routes.myrecipes }}>
                  <Typography textAlign="center">My Recipes</Typography>
                </MenuItem>}
                <MenuItem key={3} onClick={() => {window.location.href = routes.about }}>
                  <Typography textAlign="center">About</Typography>
                </MenuItem>
            </Menu>
          </Box>
          <AdbIcon sx={{ display: { xs: 'flex', md: 'none' }, mr: 1 }} />
          <Typography
            variant="h5"
            noWrap
            component="a"
            href=""
            sx={{
              mr: 2,
              display: { xs: 'flex', md: 'none' },
              flexGrow: 1,
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            LOGO
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
              <Button
                key={0}
                onClick={() => {window.location.href = `/home`}}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                Search
              </Button>
              {Object.keys(user).length > 0 && <Button
                key={1}
                onClick={() => {window.location.href = `/home`}}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                My Recipe
              </Button>}
              <Button
                key={2}
                onClick={() => {window.location.href = `/about`}}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                About
              </Button>

          </Box>
          {Object.keys(user).length == 0 ?
          <div id="signInDiv" to="/signin" /> : (
            <Box sx={{ flexGrow: 0 }}>
              <Tooltip title="User">
                <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                  <Avatar alt="User" src={user?.picture} />
                </IconButton>
              </Tooltip>
            </Box>
          )}
        </Toolbar>
      </Container>
    </AppBar>
  );
}
export default ResponsiveAppBar;
