import { createContext } from 'react'
import settings from './config'

export const AppContext = createContext({})
export const API_URL = settings.REACT_APP_API_URL;
export const getRecipeByNameURL = "/recipes/get-recipes-by-name";
export const getRecipeByAreaURL = "/recipes/get-recipes-by-area";
export const getRecipeByCategoryURL = "/recipes/get-recipes-by-category";
export const getRecipeByIngredientURL = "/ingredients/get-recipes-by-ingredients";
export const getRecipeByIdURL = "/recipes/get-recipes-by-id";
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
