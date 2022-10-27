import React, { Component } from 'react';
import RandomRecipes from './components/RandomRecipes';
import './App.css';

export default class App extends Component {
  render() {
    return (
     <div>
        <RandomRecipes/>   
     </div>
    );
  }
}