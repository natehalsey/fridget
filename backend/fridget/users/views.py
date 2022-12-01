# this file contains views pertaining directly to a user

from fastapi import APIRouter, Depends
from fridget.users.controller import UserController
from fridget.base.auth.auth import get_current_active_user
from fridget.base.schema import User
from fridget.recipes.models import RecipeModel, IngredientListModel

router = APIRouter(
    prefix="/users"
)

user_controller = UserController()


@router.post("/add-ingredient")
async def add_user_ingredient(
    ingredient: str,
    current_user: User = Depends(get_current_active_user)
):
    """
    "Add an ingredient to the current user's list of ingredients."

    :param ingredient: str - This is the ingredient that the user wants to add to their list
    :type ingredient: str
    :param current_user: User = Depends(get_current_active_user)
    :type current_user: User
    :return: The return value is a dictionary with the key "ingredient" and the value is the ingredient
    that was added.
    """
    return await user_controller.add_user_ingredient(ingredient, current_user)


@router.delete("/remove-ingredient")
async def remove_ingredient(
    ingredient: str,
    current_user: User = Depends(get_current_active_user)
):
    """
    "Remove an ingredient from the current user's list of ingredients."

    :param ingredient: str - This is the ingredient that we want to remove from the user's list of
    ingredients
    :type ingredient: str
    :param current_user: User = Depends(get_current_active_user)
    :type current_user: User
    :return: The return value is a dictionary with the following keys:
        - status: The status of the request.
        - message: A message describing the status.
        - data: The data returned by the request.
    """
    return await user_controller.remove_ingredient(ingredient, current_user)


@router.get("/get-ingredients")
async def get_user_ingredients(current_user: User = Depends(get_current_active_user)) -> IngredientListModel:
    """
    "Get the current user's ingredients."

    :param current_user: User = Depends(get_current_active_user)
    :type current_user: User
    :return: A list of ingredients
    """
    return await user_controller.get_user_ingredients(current_user)


@router.get("/get-saved-recipes", response_model=list[RecipeModel])
async def get_saved_recipes(current_user: User = Depends(get_current_active_user)):
    """
    "Get the saved recipes for the current user."

    :param current_user: User = Depends(get_current_active_user)
    :type current_user: User
    :return: A list of recipes that the user has saved.
    """
    return await user_controller.get_saved_recipes(current_user)


@router.get("/get-created-recipes", response_model=list[RecipeModel])
async def get_created_recipes(current_user: User = Depends(get_current_active_user)) -> list[RecipeModel]:
    """
    "Get all recipes created by the current user."

    :param current_user: User = Depends(get_current_active_user)
    :type current_user: User
    :return: A list of RecipeModel objects
    """
    return await user_controller.get_created_recipes(current_user)


@router.post("/save-recipe")
async def save_recipe(id: int, current_user: User = Depends(get_current_active_user)):
    """
    "Save a recipe to the current user's saved recipes."

    :param id: int - the id of the recipe to save
    :type id: int
    :param current_user: User = Depends(get_current_active_user)
    :type current_user: User
    :return: The recipe object
    """
    return await user_controller.save_recipe(id, current_user)


@router.delete("/remove-saved-recipe")
async def remove_saved_recipe(id: int, current_user: User = Depends(get_current_active_user)):
    """
    This function removes a saved recipe from the current user's saved recipes list

    :param id: int - the id of the recipe to remove
    :type id: int
    :param current_user: User = Depends(get_current_active_user)
    :type current_user: User
    :return: The return value is a dictionary with the key "message" and the value "Recipe removed from
    saved recipes"
    """
    return await user_controller.remove_saved_recipe(id, current_user)


@router.delete("/remove-created-recipe")
async def remove_created_recipe(id: int, current_user: User = Depends(get_current_active_user)):
    """
    This function removes a recipe from the current user's created recipes list

    :param id: int - the id of the recipe to be removed
    :type id: int
    :param current_user: User = Depends(get_current_active_user)
    :type current_user: User
    :return: The recipe that was removed.
    """
    return await user_controller.remove_created_recipe(id, current_user)
