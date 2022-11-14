from fastapi import APIRouter
from fridget.base.schema import RecipeIngredientMeasurement
from fridget.ingredients.models import IngredientListModel
from fridget.ingredients.controller import IngredientController

router = APIRouter(
    prefix = "/ingredients"
)

ingredient_controller = IngredientController()


@router.post("/get-recipes-by-ingredients")
async def get_recipes_by_ingredients(ingredients: IngredientListModel) -> list[RecipeIngredientMeasurement]:
    return await ingredient_controller.get_recipes_by_ingredients(ingredients)
