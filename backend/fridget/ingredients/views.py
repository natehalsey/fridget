from fastapi import APIRouter
from fridget.base.schema import Recipe
from fridget.ingredients.controller import IngredientController

router = APIRouter(
    prefix = "/ingredients"
)

ingredient_controller = IngredientController()

@router.get("/get-recipes-by-ingredients", response_model=list[Recipe])
async def get_recipes_by_ingredients(ingredients: str) -> list[Recipe]:
    return await ingredient_controller.get_recipes_by_ingredients(ingredients.split(","))
