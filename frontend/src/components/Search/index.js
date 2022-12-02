import React, { useEffect, useState } from "react";
import styles from "./styles.css";
import axios from "axios";
import RecipeCard from "../RecipeCard";
import Grid from "@mui/material/Grid";
import {
  searchParamArea,
  searchParamCategory,
  searchParamIngredient,
  searchParamName,
  endpointMap,
  AppContext,
  API_URL,
  getRandomRecipes,
} from "../../constants";

import FormControl from "@mui/material/FormControl";

import IconButton from "@mui/material/IconButton";
import Input from "@mui/material/Input";
import InputAdornment from "@mui/material/InputAdornment";
import ManageSearchIcon from "@mui/icons-material/ManageSearch";
import SearchMenu from "../SearchMenu";

/**
 * Returns a div that contains a search bar, a dropdown menu, and a grid of recipes
 * cards. Allows the use to search for recipes
 * @returns A React component
 */
const Search = () => {
  const [query, setQuery] = useState([]);
  const [searchTitle, setSearchTitle] = useState("");
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const { searchParams, setSearchParams } = React.useContext(AppContext);

  const loadQuery = async (url, params) => {
    return await axios.get(url, { params });
  };

  useEffect(() => {
    if (searchTitle) {
      const url = endpointMap.get(searchParams);
      const body = { [searchParams]: searchTitle };

      loadQuery(url, body).then((res) => setQuery(res?.data ? res.data : []));
    } else {
      const url = API_URL + getRandomRecipes;
      const body = { n: 20 };

      loadQuery(url, body).then((res) => setQuery(res?.data ? res.data : []));
    }
  }, [searchTitle, searchParams]);

  const handleOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = (value) => {
    setSearchParams(value);
    setAnchorEl(null);
  };

  return (
    <div className={styles.staticpage}>
      <div className="input-div">
        <FormControl fullWidth variant="standard">
          <Input
            id="search-input"
            className="search"
            placeholder={`Search recipes by ${searchParams === "area" ? `cuisine` : searchParams}`}
            value={searchTitle}
            onChange={(e) => setSearchTitle(e.target.value)}
            endAdornment={
              <InputAdornment onClick={handleOpen} position="end">
                <IconButton edge="end">{<ManageSearchIcon />}</IconButton>
              </InputAdornment>
            }
          />
        </FormControl>
        <SearchMenu
          selectedValue={searchParams}
          anchorEl={anchorEl}
          open={open}
          onClose={handleClose}
        />
      </div>

      <Grid container spacing={1}>
        {query.map((row) => (
          <Grid key={row?.id} item xs={12} sm={4} md={3} lg={3}>
            <RecipeCard data={row} className="list"></RecipeCard>
          </Grid>
        ))}
      </Grid>
    </div>
  );
};

export default Search;
