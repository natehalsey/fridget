
import React, { Component } from 'react';
import axios from 'axios';
import * as Constants from "./constants"
import RecipeView from './RecipeView/RecipeView';

export default class RandomRecipes extends Component {
  constructor(props) {
    super(props);
    this.state = {
      recipes: []
    }
    this.fetchRecipes = this.fetchRecipes.bind(this);
  }

  fetchRecipes() {
    axios.get(Constants.baseURL+'/random_recipe')
      .then( (response) => {
        this.setState({recipes: response.data.meals});
      })
      .catch( (error) => {
        console.log(error);
      });  
  }


  render() {
    return (
      <div>
          <button onClick={this.fetchRecipes}>Get Random Recipe</button>
          <RecipeView
            recipes={this.state.recipes}
          />
      </div>
    );
  }
}
