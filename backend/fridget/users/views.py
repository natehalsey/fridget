from fastapi import APIRouter, Response
from fridget.users.controller import UserController
from fridget.users.models import LoginRequestModel, SaveRecipeModel, UserIngredientModel
from fridget.base.schema import User, Recipe
from fridget.ingredients.models import IngredientListModel

router = APIRouter(
    prefix = "/users",
    tags=["users"],
)

user_controller = UserController()

@router.post('/login')
async def login(user_info: LoginRequestModel) -> User:
    return await user_controller.login(user_info)

@router.post("/add-ingredients")
async def add_user_ingredients(user_ingredients: UserIngredientModel) -> Response:
    return await user_controller.add_user_ingredients(user_ingredients)


@router.get("/get-ingredients")
async def get_user_ingredients(user_id: int) -> IngredientListModel:
    return await user_controller.get_user_ingredients(user_id)
        
@router.get("/get-saved-recipes")
async def get_saved_recipes(user_id: int) -> list[Recipe]:
    return await user_controller.get_saved_recipes(user_id)
    
@router.get("/get-created-recipes")
async def get_created_recipes(user_id: int) -> list[Recipe]:
    return await user_controller.get_created_recipes(user_id)

@router.post("/save-recipe")
async def save_recipe(save_recipe: SaveRecipeModel) -> Response:
    return await user_controller.save_recipe(save_recipe)

# debugging only, remove before prod
@router.get("/get-users")
async def get_users() -> list[User]:
    return await user_controller.get_users()

