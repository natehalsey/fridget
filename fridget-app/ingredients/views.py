import ormar
from fastapi import APIRouter
from ..recipes.requests import RequestRecipes
from ..base.schema import Recipe
from .model import Ingredient

router = APIRouter(
    prefix = "/ingredients"
)

@router.get("/my_recipes")
async def get_personal_recipe_from_ingredients(ingredients:list[Ingredient]) -> list[Recipe]:
    # check database for recipes matching
    # return list of recipes
    pass


@router.get("/api_recipes")
async def get_api_recipe_from_ingredients(ingredients: list[ingredient]) -> list[Recipe]:
    # request recipes
    # parse as list of recipes
    # return recipes
    pass

@router.get("/both")
async def get_both_recipe_from_ingredients(ingredients: list[ingredient]) -> list[Recipe]:
    # request recipes and parse as list
    # check database and create a list
    # return union of both
    pass
