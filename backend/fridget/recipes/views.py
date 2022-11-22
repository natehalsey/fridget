from fastapi import APIRouter, Response
from fridget.base.schema import Recipe
from fridget.recipes.models import RecipeModel
from fridget.users.models import UserRecipeModel
from fridget.recipes.controller import RecipeController

    
router = APIRouter(
    prefix = "/recipes"
)
@router.get("/get-recipes-by-name")
async def get_recipes_by_name(name: str) -> list[RecipeModel]:
    return await RecipeController.get_recipes_by_name(name)

@router.get("/get-recipe-by-id")
async def get_recipe_by_id(id: int) -> RecipeModel:
    return await RecipeController.get_recipe_by_id(id)

@router.get("/get-recipes-by-random")
async def get_recipes_by_random(n: int) -> list[RecipeModel]:
    return await RecipeController.get_recipes_by_random(n)

@router.post("/create-recipe")
async def create_recipe(user_recipe: UserRecipeModel):
    
    await RecipeController.create_recipe(user_recipe)
    return Response(status_code=200)
        
@router.get("/get-recipes-by-category")
async def get_recipes_by_category(category: str) -> list[RecipeModel]:
    return await Recipe.objects.filter(
        category__name__contains=category
    ).all()


    
@router.get("/get-recipes-by-area")
async def get_recipes_by_area(area: str) -> list[RecipeModel]:
    return await Recipe.objects.filter(
        area__name__contains=area
    ).all()
    