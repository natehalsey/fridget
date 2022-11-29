import { createContext } from 'react'
import settings from './config'
import { createTheme } from '@mui/material/styles';

export const AppContext = createContext({})
export const theme = createTheme({
  palette: {
    primary: {
      light: '#757ce8',
      main: '#3f50b5',
      dark: '#002884',
      contrastText: '#fff',
    },
    secondary: {
      light: '#ff7961',
      main: '#f44336',
      dark: '#ba000d',
      contrastText: '#000',
    },
  },
  breakpoints: {
    values: {
      xs: 0,
      sm: 500,
      md: 900,
      lg: 1200,
      xl: 1536,
    },
  },
});
export const API_URL = settings.REACT_APP_API_URL;
export const loginURL = "/auth/login"
export const logoutURL = "/auth/logout"
export const signupURL = "/auth/sign-up"
export const getRecipeByNameURL = "/recipes/get-recipes-by-name";
export const getRecipeByAreaURL = "/recipes/get-recipes-by-area";
export const getRecipeByCategoryURL = "/recipes/get-recipes-by-category";
export const getRecipeByIngredientURL = "/ingredients/get-recipes-by-ingredients";
export const getRecipeByIdURL = "/recipes/get-recipe-by-id";
export const getRandomRecipes = "/recipes/get-recipes-by-random";
export const postUserData = "/users/login"
export const searchParamName = "name";
export const searchParamArea = "area";
export const searchParamCategory = "category";
export const searchParamIngredient = "ingredients";
export const endpointMap = new Map([
    [searchParamName, API_URL + getRecipeByNameURL],
    [searchParamArea, API_URL + getRecipeByAreaURL],
    [searchParamCategory, API_URL + getRecipeByCategoryURL],
    [searchParamIngredient, API_URL + getRecipeByIngredientURL]
  ]);
export const routes = {
  home: "/home",
  myrecipes: "/myrecipes",
  about: "/about",
  login: "/login",
  signup: "/signup",
};
