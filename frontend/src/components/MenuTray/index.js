import React from "react";
import { MenuItem } from "@mui/material";
import { AppContext } from "../../constants";
import { useNavigate } from "react-router-dom";
import "./styles.css";
import axios from "axios";
import { API_URL, logoutURL, routes } from "../../constants";

/**
 * The MenuTray function is a React component that renders a menu tray with menu items when the user in on a mobile device
 *
 */
const MenuTray = () => {
  const { showMenu, setShowMenu, menuItems } = React.useContext(AppContext);

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
  let navigate = useNavigate();
  return (
    <div className="tray">
      {showMenu && (
        <MenuItem
          onClick={() => {
            navigate(routes.home);
          }}
        >
          Search
        </MenuItem>
      )}
      {showMenu &&
        menuItems.menu_items.map((menu_item) => {
          return (
            <MenuItem
              onClick={() => {
                menu_item.click ? navigate(menu_item.click) : handleLogout();
                setShowMenu(false);
              }}
            >
              {menu_item.item}
            </MenuItem>
          );
        })}
    </div>
  );
};
export default MenuTray;
