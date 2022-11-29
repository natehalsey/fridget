import { MenuItem } from '@mui/material';
import React from 'react';
import MenuIcon from '@mui/icons-material/Menu';
import Box from '@mui/material/Box';
import { AppContext } from '../../constants';


const DropDownMenu = (menu_items) => {
    const { showMenu, setShowMenu, setMenuItems } = React.useContext(AppContext);
    const toggleMenu = () => {
        setShowMenu(!showMenu)
        setMenuItems(menu_items)
    }
    return ( 
        <Box>
            <div>
            <button onClick={toggleMenu}>
             <MenuIcon></MenuIcon>
            </button>
            </div>
        </Box>
    );
}
export default DropDownMenu