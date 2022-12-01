import { MenuItem } from "@mui/material";
import React from "react";
import MenuIcon from "@mui/icons-material/Menu";
import Box from "@mui/material/Box";
import { AppContext } from "../../constants";
import "./styles.css";

/**
 * It's a function that takes in an array of menu items, and returns a button that toggles the menu
 * items in the AppContext
 * @param menu_items - an array of objects that contain the following properties:
 * @returns A button that when clicked will toggle the menu items.
 */
const DropDownMenu = (menu_items) => {
  const { showMenu, setShowMenu, setMenuItems } = React.useContext(AppContext);
  const toggleMenu = () => {
    setShowMenu(!showMenu);
    setMenuItems(menu_items);
  };
  return (
    <Box>
      <div>
        <button className="tray-button" onClick={toggleMenu}>
          <MenuIcon></MenuIcon>
        </button>
      </div>
    </Box>
  );
};
export default DropDownMenu;
