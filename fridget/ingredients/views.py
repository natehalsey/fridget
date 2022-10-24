import ormar
from fastapi import APIRouter
from ..recipes.requests import RequestRecipes
from ..base.schema import Recipes
from .models import Ingredients
from typing import List

router = APIRouter(
    prefix = "/ingredients"
)

@router.get("/my_recipes")
async def get_personal_recipe_from_ingredients(ingredients:List[Ingredients]) -> List[Recipes]:
    # check database for recipes matching
    # return list of recipes
    pass


@router.get("/api_recipes")
async def get_api_recipe_from_ingredients(ingredients: List[Ingredients]) -> List[Recipes]:
    # request recipes
    # parse as list of recipes
    # return recipes
    pass

@router.get("/both")
async def get_both_recipe_from_ingredients(ingredients: List[Ingredients]) -> List[Recipes]:
    # request recipes and parse as list
    # check database and create a list
    # return union of both
    pass
