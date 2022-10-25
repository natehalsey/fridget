import React, { Component } from 'react';
import axios from 'axios';

class Recipe extends Component {
  render() {
    return (
        <div>
            <div>Recipe id: {this.props.recipeId}</div>
            <div>Recipe Name: {this.props.recipeName}</div>
        </div>
    );
  }
}

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fetchRecipe: {
        recipeId: 'N/A',
        recipeName: 'N/A'
      }
    }
    this.fetchRecipe = this.fetchRecipe.bind(this);
  }

  fetchRecipe() {
    axios.get('http://localhost:8000/random_recipe')
      .then( (response) => {
        console.log("response", response);
        this.setState({
          fetchRecipe: {
            recipeId: response.data.meals[0].idMeal, 
            recipeName: response.data.meals[0].strMeal
          }});
        console.log("fetchRecipe", this.state.fetchRecipe);
      })
      .catch( (error) => {
        console.log(error);
      });  
  }


  render() {
    return (
      <div>
          <button onClick={this.fetchRecipe}>Get Random Recipe</button>
          <Recipe
            recipeId={this.state.fetchRecipe.recipeId} 
            recipeName={this.state.fetchRecipe.recipeName} 
          />
      </div>
    );
  }
}

export default App;
