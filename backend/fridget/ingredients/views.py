from sqlite3 import IntegrityError
from fastapi import APIRouter, HTTPException
from fridget.base.schema import Ingredient, RecipeIngredientMeasurement
from fridget.ingredients.models import IngredientModel, IngredientQueryModel
router = APIRouter(
    prefix = "/ingredients"
)
 
@router.get("/get-all-ingredients")
async def get_all_ingredients():
    return await Ingredient.objects.all()


@router.post("/create-ingredient")
async def create_ingredient(ingredient_model: IngredientModel):
    try:
        await Ingredient.objects.create(
            name=ingredient_model.name,
            description=ingredient_model.description,
            type=ingredient_model.type
        )
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Ingredient already exists: {e}")


@router.get("/search-by-ingredients")
async def search_by_ingredients(ingredients: IngredientQueryModel):
    return await RecipeIngredientMeasurement.objects.select_related("ingredient").filter(
        ingredient__name__in=ingredients.ingredients
    ).select_related("recipe").all()
