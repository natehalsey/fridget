import { Button, Typography } from '@mui/material';
import { color } from '@mui/system';
import React from 'react';
import UserSavedRecipes from '../components/UserSavedRecipes';
import UserCreatedRecipes from '../components/UserCreatedRecipes';
import { useNavigate } from 'react-router-dom';
import { routes } from "../constants"

const MyRecipes = () => {
  let navigate = useNavigate()
  return (<div className='MyRecipesPage'>
    <Button onClick={() => {navigate(routes.create)}}>
        Create Recipe
    </Button>
    <Typography variant="h4">
        Saved Recipes
    </Typography>
    <UserSavedRecipes/>
    <Typography variant="h4">
        Created Recipes
    </Typography>
    <UserCreatedRecipes/>
  </div>
  );
};
export default MyRecipes;