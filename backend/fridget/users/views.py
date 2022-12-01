from fastapi import APIRouter, Depends
from fridget.users.controller import UserController
from fridget.base.auth.auth import get_current_active_user
from fridget.base.schema import User
from fridget.recipes.models import RecipeModel, IngredientListModel

router = APIRouter(
    prefix="/users"
)

user_controller = UserController()

# this file contains views pertaining directly to a user
@router.post("/add-ingredient")
async def add_user_ingredient(
    ingredient: str, 
    current_user: User = Depends(get_current_active_user)
):
    return await user_controller.add_user_ingredient(ingredient, current_user)

@router.delete("/remove-ingredient")
async def remove_ingredient(
    ingredient: str,
    current_user: User = Depends(get_current_active_user)
):
    return await user_controller.remove_ingredient(ingredient, current_user)

@router.get("/get-ingredients")
async def get_user_ingredients(current_user: User = Depends(get_current_active_user)) -> IngredientListModel:
    return await user_controller.get_user_ingredients(current_user)

@router.get("/get-saved-recipes", response_model=list[RecipeModel])
async def get_saved_recipes(current_user: User = Depends(get_current_active_user)):
    return await user_controller.get_saved_recipes(current_user)

@router.get("/get-created-recipes", response_model=list[RecipeModel])
async def get_created_recipes(current_user: User = Depends(get_current_active_user)) -> list[RecipeModel]:
    return await user_controller.get_created_recipes(current_user)
    
@router.post("/save-recipe")
async def save_recipe(id: int, current_user: User = Depends(get_current_active_user)):
    return await user_controller.save_recipe(id, current_user)


@router.delete("/remove-saved-recipe")
async def remove_saved_recipe(id: int, current_user: User = Depends(get_current_active_user)):
    return await user_controller.remove_saved_recipe(id, current_user)


@router.delete("/remove-created-recipe")
async def remove_created_recipe(id: int, current_user: User = Depends(get_current_active_user)):
    return await user_controller.remove_created_recipe(id, current_user)