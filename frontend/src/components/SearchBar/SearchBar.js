import React, { useEffect, useState } from "react";
import styles from "./SearchBar.css";
import axios from "axios";
import MediaCard from  "../Card/Card";
import Grid from '@mui/material/Grid';
import { AppContext } from "../../AppContext"
import { baseURL, 
  getRecipeByAreaURL, 
  getRecipeByCategoryURL, 
  getRecipeByIngredientURL, 
  getRecipeByNameURL } from "../../constants";

const SearchBar = () => {
  const [query, setQuery] = useState([]);
  const [searchTitle, setSearchTitle] = useState("");
  const {searchParams} = React.useContext(AppContext)
  

  useEffect(() => {
    console.log(searchParams);
    let url = baseURL + getRecipeByNameURL;
    let body = { "name": searchTitle };

    if (searchParams === "name") {
      url = baseURL + getRecipeByNameURL;
      body = { "name": searchTitle}
    } else if (searchParams === "area") {
      url = baseURL + getRecipeByAreaURL;
      body = { "area": [searchTitle] };
    } else if (searchParams === "category") {
      url = baseURL + getRecipeByCategoryURL;
      body = { "category": [searchTitle] };
    } else if (searchParams === "ingredient"){
      url = baseURL + getRecipeByIngredientURL;
      body = { "ingredient": [searchTitle] };
    }

    const loadQuery = async (url, body) => {
      const response = await axios.post(url, body);
      if (response.data) {
        setQuery(response.data);
      }
      
    };

    loadQuery(url, body);
  }, [searchTitle, searchParams]);

  return (
    <div className={styles.staticpage}>
      <input
        type="text"
        placeholder="Search..."
        className="search"
        onChange={(e) => setSearchTitle(e.target.value)}
      />
      <Grid container spacing={2}>
        {query
          .map((row) => (
              <Grid item xs={3}>
                <MediaCard data={row} className="list"></MediaCard>
              </Grid>
          ))}
      </Grid>
    </div>
  );
};

export default SearchBar;
