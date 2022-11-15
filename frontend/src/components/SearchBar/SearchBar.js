import React, { useEffect, useState } from "react";
import styles from "./SearchBar.css";
import axios from "axios";
import RecipeCard from  "../RecipeCard/RecipeCard";
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

  const loadQuery = async (url, body) => {
    return await axios.post(url, body);
  };


  useEffect(() => {
    let url = baseURL + getRecipeByNameURL;
    let body = { "name": searchTitle };

    if (searchParams === "name") {
      url = baseURL + getRecipeByNameURL;
      body = { "name": searchTitle}
      
      loadQuery(url, body).then(
        (res) => setQuery(res?.data ? res.data : [])
        );

    } else if (searchParams === "area") {
      url = baseURL + getRecipeByAreaURL;
      body = { "areas": [searchTitle] };

      loadQuery(url, body).then(
        (res) => setQuery(res?.data.length > 0 ? res.data[0].recipes : [])
        );


    } else if (searchParams === "category") {
      url = baseURL + getRecipeByCategoryURL;
      body = { "categories": [searchTitle] };

      loadQuery(url, body).then(
        (res) => setQuery(res?.data ? res.data.recipes : [])
        );

    } else if (searchParams === "ingredient"){
      url = baseURL + getRecipeByIngredientURL;
      body = { "ingredients": searchTitle.split(",") };

      loadQuery(url, body).then(
        (res) => setQuery(res?.data ? res.data : [])
        );
    }
   
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
                <RecipeCard data={row} className="list"></RecipeCard>
              </Grid>
          ))}
      </Grid>
    </div>
  );
};

export default SearchBar;
