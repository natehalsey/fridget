import React, { useState } from 'react';
import axios from 'axios';
import { API_URL, AppContext } from '../../constants';
import RecipeCard from '../RecipeCard';
import { Grid } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const UserCreatedRecipes = () => {
  const [createdRecipes, setCreatedRecipes] = React.useState([])
  let navigate = useNavigate();

  
  React.useEffect(() => {
   
          getSavedRecipes();
    },[]);


    const getSavedRecipes = () => { 
        axios({
            method: "get",
            url: API_URL + "/users/get-created-recipes",
            headers: {"Content-Type": 'application/json'},
        }).then( (response) => {
            setCreatedRecipes(response.data)
        })
        .catch( (error) => {
            console.log(error);
            localStorage.setItem("auth", false)
            navigate("/home")
        });
    };

  return (<div>
      <Grid container disableGutters={true} spacing={1}>
        {createdRecipes
          .map((row) => (
              <Grid key={row?.id} item xs={12} sm={4} md={3} lg={3}>
                <RecipeCard data={row} className="list"></RecipeCard>
              </Grid>
          ))}
      </Grid>
  </div>
  );
};
export default UserCreatedRecipes;