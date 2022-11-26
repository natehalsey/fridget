import { createContext } from 'react'

export const AppContext = createContext({})
export const baseURL = "http://0.0.0.0:8000"; // if local 8000, if prod 81
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
    [searchParamName, baseURL + getRecipeByNameURL],
    [searchParamArea, baseURL + getRecipeByAreaURL],
    [searchParamCategory, baseURL + getRecipeByCategoryURL],
    [searchParamIngredient, baseURL + getRecipeByIngredientURL]
  ]);
