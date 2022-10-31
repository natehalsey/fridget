import axios from 'axios';
import * as Constants from "./constants"

export default function fetchRecipes(path){
  axios.get(Constants.baseURL+path)
    .then( (response) => {
      return response.data.meals;
    })
    .catch( (error) => {
      console.log(error);
    });  
}
