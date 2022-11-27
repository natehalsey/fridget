import React from 'react';


const UserRecipes = () => {
  return (<div>
    <a href="/create">
      Create Recipe
    </a>
    <br/>
    <a href="/fridget">
      Add Item to Fridget
    </a>
    <p>list of user saved recipe</p>
    <p>list of user created recipe</p>
  </div>
  );
};
export default UserRecipes;