import * as React from "react";
import MenuItem from "@mui/material/MenuItem";
import Menu from "@mui/material/Menu";
import {
  searchParamArea,
  searchParamCategory,
  searchParamIngredient,
  searchParamName,
  endpointMap,
} from "../../constants";

/**
 * This function is a dropdown menu that allows the user to select a search parameter
 * @param props - the menu props that control is functionality
 * @returns A menu that allows the user to select a search parameter.
 */
export default function SearchMenu(props) {
  const { onClose, selectedValue, open, anchorEl } = props;

  const handleClose = () => {
    onClose(selectedValue);
  };

  const handleMenuItemClick = (value) => {
    onClose(value);
  };

  return (
    <Menu onClose={handleClose} anchorEl={anchorEl} open={open}>
      <MenuItem button onClick={() => handleMenuItemClick(searchParamName)}>
        Search by Name
      </MenuItem>
      <MenuItem button onClick={() => handleMenuItemClick(searchParamArea)}>
        Search by Cuisine
      </MenuItem>
      <MenuItem button onClick={() => handleMenuItemClick(searchParamCategory)}>
        Search by Category
      </MenuItem>
      <MenuItem
        button
        onClick={() => handleMenuItemClick(searchParamIngredient)}
      >
        Search by Ingredients
      </MenuItem>
    </Menu>
  );
}
