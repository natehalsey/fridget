import * as React from 'react';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import { 
    searchParamArea, 
    searchParamCategory, 
    searchParamIngredient, 
    searchParamName, 
    endpointMap, 
  } from "../../constants";

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
            <MenuItem button onClick={() => handleMenuItemClick(searchParamIngredient)}>
                Search by Ingredient
            </MenuItem>
            {1 !== 0 && ( 
                <>
                    <MenuItem button onClick={() => {window.location.href = `/create`}}>
                        Create Recipe
                    </MenuItem>
                    <MenuItem button onClick={() => {window.location.href = `/fridget`}}>
                        Add Item to Fridget
                    </MenuItem>
                </>)}
        </Menu>
    );
  }