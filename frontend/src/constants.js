import { createContext } from 'react'

export const AppContext = createContext({})
export const baseURL = "http://localhost:8000";
export const getRecipeByNameURL = "/recipes/get-recipes-by-name";
export const getRecipeByAreaURL = "/recipes/get-recipes-by-area";
export const getRecipeByCategoryURL = "/recipes/get-recipes-by-category";
export const getRecipeByIngredientURL = "/ingredients/get-recipes-by-ingredients";
export const getRecipeByIdURL = "/recipes/get-recipes-by-id";
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
