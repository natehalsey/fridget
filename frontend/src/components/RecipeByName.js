
import React, { Component } from 'react';
import axios from 'axios';
import * as Constants from "./constants"
import RecipeView from "./RecipeView/RecipeView"

export default class RecipeByName extends Component {
  constructor(props) {
    super(props);
    this.state = {
      recipes: []
    }
    this.fetchRecipe = this.fetchRecipe.bind(this);
  }

  fetchRecipe() {
    axios.get(Constants.baseURL+'/random_recipe')
      .then( (response) => {
        this.setState({
            recipes: response.data.meals 
          });
      })
      .catch( (error) => {
        console.log(error);
      });  
  }


  render() {
    return (
      <div>
          <RecipeView
            recipes={this.state.recipes}
          />
          <button onClick={this.fetchRecipe}>Get Random Recipe</button>
      </div>
    );
  }
}