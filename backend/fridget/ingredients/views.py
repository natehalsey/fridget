from fastapi import APIRouter
from fridget.recipes.models import RecipeModel
from fridget.ingredients.controller import IngredientController

router = APIRouter(
    prefix = "/ingredients"
)

ingredient_controller = IngredientController()

@router.get("/get-recipes-by-ingredients", response_model=list[RecipeModel])
async def get_recipes_by_ingredients(ingredients: str) -> list[RecipeModel]:
    return await ingredient_controller.get_recipes_by_ingredients(ingredients.split(","))
