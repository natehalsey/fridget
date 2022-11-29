import ormar
from fastapi import APIRouter, Depends, status, HTTPException
from fridget.users.controller import UserController
from fridget.users.models import UserModel
from fridget.base.auth.auth import get_current_active_user
from fridget.base.schema import Recipe, User
from fridget.recipes.models import RecipeModel, IngredientListModel

router = APIRouter(
    prefix="/users"
)

user_controller = UserController()
@router.post("/add-ingredients")
async def add_user_ingredients(
    ingredients: IngredientListModel, 
    current_user: User = Depends(get_current_active_user)
):
    return await user_controller.add_user_ingredients(ingredients, current_user)


@router.get("/get-ingredients", response_model=IngredientListModel)
async def get_user_ingredients(current_user: User = Depends(get_current_active_user)) -> IngredientListModel:
    return await user_controller.get_user_ingredients(current_user)

@router.get("/get-saved-recipes")
async def get_saved_recipes(current_user: User = Depends(get_current_active_user)):
    return await user_controller.get_saved_recipes(current_user)

@router.get("/get-created-recipes", response_model=list[RecipeModel])
async def get_created_recipes(current_user: User = Depends(get_current_active_user)) -> list[RecipeModel]:
    return await user_controller.get_created_recipes(current_user)
    
@router.post("/save-recipe")
async def save_recipe(id: int, current_user: User = Depends(get_current_active_user)):
    return await user_controller.save_recipe(id, current_user)


@router.post("/remove-recipe")
async def remove_recipe(id: int, current_user: User = Depends(get_current_active_user)):
    return await user_controller.remove_recipe(id, current_user)
