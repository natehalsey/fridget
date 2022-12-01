import ormar
from fastapi import status, HTTPException, Response
from fridget.recipes.models import IngredientListModel
from fridget.base.schema import Recipe, User, UserSavedRecipe, UserCreatedRecipe, Ingredient, UserIngredient


# user controller controls all user actions
class UserController:
    async def add_user_ingredient(self, ingredient: str, current_user: User):
        """
        Adds an ingredient to the current user's list of ingredients

        :param ingredient: str - the name of the ingredient to add
        :type ingredient: str
        :param current_user: User - this is the user that is currently logged in
        :type current_user: User
        :return: The response object is being returned.
        """
        ingredient, _ = await Ingredient.objects.get_or_create(name=ingredient)
        await UserIngredient.objects.create(
            user=current_user,
            ingredient=ingredient
        )
        return Response(status_code=status.HTTP_201_CREATED)

    async def remove_ingredient(self, ingredient: str, current_user: User):
        """
        Remove an ingredient from the current user's list of ingredients

        :param ingredient: str - This is the name of the ingredient that we want to remove from the
        user's list
        :type ingredient: str
        :param current_user: User - this is the current user that is logged in
        :type current_user: User
        :return: The response object is being returned.
        """
        ingredient = await Ingredient.objects.get(
            name=ingredient
        )
        await UserIngredient.objects.delete(
            user=current_user,
            ingredient=ingredient
        )
        return Response(status_code=status.HTTP_200_OK)

    async def get_user_ingredients(self, current_user: User) -> IngredientListModel:
        """
        Get all the ingredients for the current user

        :param current_user: User - This is the user that is currently logged in
        :type current_user: User
        :return: A list of ingredients
        """
        user_ingredients = await UserIngredient.objects.select_related("ingredient").fields("ingredient").filter(
            user=current_user
        ).all()

        return IngredientListModel(
            ingredients=[
                user_ingredient.ingredient.name
                for user_ingredient in user_ingredients
            ]
        )

    async def get_saved_recipes(self, current_user: User):
        """
        "Get all the recipes that the current user has saved."

        The first line of the function is a docstring. It's a string that describes what the function does.
        It's a good idea to include a docstring for every function you write

        :param current_user: User
        :type current_user: User
        :return: A list of recipes that the user has saved.
        """
        user_saved_recipes = await UserSavedRecipe.objects.select_related("recipe").filter(
            user=current_user
        ).all()
        return [user_saved_recipe.recipe for user_saved_recipe in user_saved_recipes]

    async def get_created_recipes(self, current_user: User):
        """
        "Get all the recipes that the current user has created."

        :param current_user: User
        :type current_user: User
        :return: A list of recipes
        """
        user_created_recipes = await UserCreatedRecipe.objects.select_related("recipe").filter(
            user=current_user
        ).all()
        return [user_created_recipe.recipe for user_created_recipe in user_created_recipes]

    async def save_recipe(self, recipe_id: int, current_user: User):
        """
        Save a recipe to the current user's saved recipes

        :param recipe_id: The id of the recipe to save
        :type recipe_id: int
        :param current_user: This is the user that is currently logged in
        :type current_user: User
        :return: The response is a list of recipes that are saved by the user.
        """
        try:
            recipe = await Recipe.objects.get(
                id=recipe_id
            )
        except ormar.NoMatch:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

        await UserSavedRecipe.objects.create(
            user=current_user,
            recipe=recipe,
        )
        return Response(status_code=status.HTTP_200_OK)

    async def remove_saved_recipe(self, recipe_id: int, current_user: User):
        """
        Remove a saved recipe from the current user's saved recipes

        :param recipe_id: The ID of the recipe to remove from the user's saved recipes
        :type recipe_id: int
        :param current_user: This is the user that is currently logged in
        :type current_user: User
        :return: The response is being returned.
        """
        try:
            recipe = await Recipe.objects.get(
                id=recipe_id
            )
        except ormar.NoMatch:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

        await UserSavedRecipe.objects.delete(
            user=current_user,
            recipe=recipe,
        )
        return Response(status_code=status.HTTP_200_OK)

    async def remove_created_recipe(self, recipe_id: int, current_user: User):
        """
        This function deletes a recipe from the database, and also deletes all the user saved recipes that
        are associated with the recipe

        :param recipe_id: The id of the recipe to be deleted
        :type recipe_id: int
        :param current_user: This is the user that is currently logged in
        :type current_user: User
        :return: The response is being returned.
        """
        try:
            recipe = await Recipe.objects.get(
                id=recipe_id
            )
        except ormar.NoMatch:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

        try:
            user_created_recipe = await UserCreatedRecipe.objects.get(
                user=current_user,
                recipe=recipe,
            )

        except ormar.NoMatch:
            raise HTTPException(
                status_code=status.HTTP_401_NOT_AUTHORIZED, detail="Not authorized")

        await user_created_recipe.delete()

        await UserSavedRecipe.objects.delete(
            recipe=recipe
        )
        await recipe.delete()

        return Response(status_code=status.HTTP_200_OK)
