from sqlite3 import IntegrityError
from fastapi import APIRouter, HTTPException, Response
from fridget.base.schema import Ingredient, RecipeIngredientMeasurement
from fridget.ingredients.models import IngredientModel, IngredientListModel
from fridget.ingredients.controller import IngredientController

router = APIRouter(
    prefix = "/ingredients"
)

ingredient_controller = IngredientController()

@router.get("/get-all-ingredients")
async def get_all_ingredients() -> list[Ingredient]:
    return await ingredient_controller.get_all_ingredients()


@router.post("/create-ingredient")
async def create_ingredient(ingredient_model: IngredientModel):
    try:
        ingredient_controller.create_ingredient(ingredient_model)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Ingredient already exists: {e}")

    return Response(status_code=200)

@router.get("/search-by-ingredients")
async def search_by_ingredients(ingredients: IngredientListModel) -> list[RecipeIngredientMeasurement]:
    return await ingredient_controller.search_by_ingredients(ingredients)
