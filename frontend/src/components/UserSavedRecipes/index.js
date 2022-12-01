import React, { useState } from "react";
import axios from "axios";
import { API_URL, AppContext } from "../../constants";
import RecipeCard from "../RecipeCard";
import { Grid } from "@mui/material";
import { useNavigate } from "react-router-dom";

/**
 * This function is used to display the saved recipes of the user
 * @returns A list of recipes that the user has saved.
 */
const UserSavedRecipes = () => {
  const [savedRecipes, setSavedRecipes] = React.useState([]);
  let navigate = useNavigate();

  React.useEffect(() => {
    getSavedRecipes();
  }, []);

  const getSavedRecipes = () => {
    axios({
      method: "get",
      url: API_URL + "/users/get-saved-recipes",
      headers: { "Content-Type": "application/json" },
    })
      .then((response) => {
        setSavedRecipes(response.data);
      })
      .catch((error) => {
        console.log(error);
        localStorage.setItem("auth", false);
        navigate("/home");
      });
  };

  return (
    <div>
      <Grid container disableGutters={true} spacing={1}>
        {savedRecipes.map((row) => (
          <Grid key={row?.id} item xs={12} sm={4} md={3} lg={3}>
            <RecipeCard data={row} className="list"></RecipeCard>
          </Grid>
        ))}
      </Grid>
    </div>
  );
};
export default UserSavedRecipes;
