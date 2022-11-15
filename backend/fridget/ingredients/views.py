from fastapi import APIRouter
from fridget.base.schema import RecipeIngredientMeasurement
from fridget.ingredients.models import IngredientListModel
from fridget.ingredients.controller import IngredientController

router = APIRouter(
    prefix = "/ingredients"
)

ingredient_controller = IngredientController()


@router.get("/get-recipes-by-ingredients")
async def get_recipes_by_ingredients(ingredients: str) -> list[RecipeIngredientMeasurement]:
    return await ingredient_controller.get_recipes_by_ingredients(ingredients.split(","))
