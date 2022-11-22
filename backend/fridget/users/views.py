from fastapi import APIRouter, Response, Depends
from fridget.users.controller import UserController
from fridget.users.models import LoginRequestModel, SaveRecipeModel, UserIngredientModel
from fridget.base.schema import User, Recipe
from fridget.ingredients.models import IngredientListModel
from fridget.base.authorization import get_token_header, get_query_token

router = APIRouter(
    prefix = "/users",
    tags=["users"],
    #dependencies=[Depends(get_token_header)]
)


@router.post('/login')
async def login(user_info: LoginRequestModel) -> User:
    return await UserController.login(user_info)

@router.post("/add-ingredients")
async def add_user_ingredients(user_ingredients: UserIngredientModel) -> Response:
    return await UserController.add_user_ingredients(user_ingredients)


@router.get("/get-ingredients")
async def get_user_ingredients(user_id: int) -> IngredientListModel:
    return await UserController.get_user_ingredients(user_id)
        
@router.get("/get-saved-recipes")
async def get_saved_recipes(user_id: int) -> list[Recipe]:
    return await UserController.get_saved_recipes(user_id)
    
@router.get("/get-created-recipes")
async def get_created_recipes(user_id: int) -> list[Recipe]:
    return await UserController.get_created_recipes(user_id)

@router.post("/save-recipe")
async def save_recipe(save_recipe: SaveRecipeModel) -> Response:
    return await UserController.save_recipe(save_recipe)

# debugging only, remove before prod
@router.get("/get-users")
async def get_users() -> list[User]:
    return await UserController.get_users()

