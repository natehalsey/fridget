import ormar
from fastapi import APIRouter
from ..recipes.requests import RequestRecipes
from ..base.schema import Recipes
from typing import List

router = APIRouter(
    prefix = "/recipes"
)

@router.put("/create")
async def create_recipe(): #some json goes in here
    # create a recipe given a user created json object
    pass

@router.get("/my_recipes")
async def search_personal_recipes_by_name(name: str) -> List[Recipes]:
    # check database for recipes matching
    # return list of recipes
    pass


@router.get("/api_recipes")
async def search_api_recipes_by_name(name: str) -> List[Recipes]:
    # request recipes
    # parse as list of recipes
    # return recipes
    pass

@router.get("/both")
async def search_both_by_name(name: str) -> List[Recipes]:
    # request recipes and parse as list
    # check database and create a list
    # return union of both
    pass