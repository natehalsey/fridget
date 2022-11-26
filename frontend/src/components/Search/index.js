import React, { useEffect, useState } from "react";
import styles from "./styles.css";
import axios from "axios";
import RecipeCard from  "../RecipeCard";
import Grid from '@mui/material/Grid';
import { endpointMap, AppContext, API_URL, getRandomRecipes } from "../../constants";

const Search = () => {
  const [query, setQuery] = useState([]);
  const [searchTitle, setSearchTitle] = useState("");
  const {searchParams} = React.useContext(AppContext)
  
  const loadQuery = async (url, params) => {
    return await axios.get(url, {params});
  };

  useEffect(() => {
    if (searchTitle) {
      const url = endpointMap.get(searchParams);
      const body = { [searchParams]: searchTitle };
      
      loadQuery(url, body).then(
        (res) => setQuery(res?.data ? res.data : [])
      );
    } else {
      const url = API_URL + getRandomRecipes;
      const body = { n: 20 };
    
      loadQuery(url, body).then(
        (res) => setQuery(res?.data ? res.data : [])
      );
    }
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
              <Grid key={row?.id} item xs={3}>
                <RecipeCard data={row} className="list"></RecipeCard>
              </Grid>
          ))}
      </Grid>
    </div>
  );
};

export default Search;
