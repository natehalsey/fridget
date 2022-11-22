from fastapi import APIRouter
from fridget.base.schema import RecipeIngredientMeasurement
from fridget.ingredients.controller import IngredientController

router = APIRouter(
    prefix = "/ingredients"
)

@router.get("/get-recipes-by-ingredients")
async def get_recipes_by_ingredients(ingredients: str) -> list[RecipeIngredientMeasurement]:
    return await IngredientController.get_recipes_by_ingredients(ingredients.split(","))
