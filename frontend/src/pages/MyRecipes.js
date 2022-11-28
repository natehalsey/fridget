import { Button, Typography } from '@mui/material';
import { color } from '@mui/system';
import React from 'react';
import UserSavedRecipes from '../components/UserSavedRecipes';
import UserCreatedRecipes from '../components/UserCreatedRecipes';

const MyRecipes = () => {
  return (<div className='MyRecipesPage'>
    <Button>
        Create Recipe
    </Button>
    <Button>
        Add Items to Fridge
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