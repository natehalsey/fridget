from fastapi import APIRouter, HTTPException, Response
from fridget.base.schema import Recipe
from fridget.recipes.models import RecipeModel
from fridget.users.models import UserRecipeModel
from fridget.recipes.controller import RecipeController

    
router = APIRouter(
    prefix = "/recipes"
)

recipe_controller = RecipeController()

@router.get("/get-recipes-by-name")
async def get_recipes_by_name(name: str) -> list[RecipeModel]:
    return await recipe_controller.filter_recipe_by_name(name)

@router.get("/get-recipes-by-id")
async def get_recipes_by_id(id: int) -> RecipeModel:
    return await recipe_controller.filter_recipe_by_id(id)

@router.get("/get-recipes-by-random")
async def get_random_recipes(n: int) -> Recipe:
    return await recipe_controller.filter_recipe_by_random(n)

@router.post("/create-recipe")
async def create_recipe(user_recipe: UserRecipeModel):
    
    try:
        await recipe_controller.create_recipe(user_recipe)
        
    except TypeError as e:
        raise HTTPException(status_code=400, detail=e)
    
    return Response(status_code=200)
    
    
@router.get("/get-recipes-by-category")
async def get_recipes_by_category(category: str) -> list[RecipeModel]:
    print(category)
    return await Recipe.objects.filter(
        category__name__contains=category
    ).all()


    
@router.get("/get-recipes-by-area")
async def get_recipes_by_area(area: str) -> list[RecipeModel]:
    print(area)
    return await Recipe.objects.filter(
        area__name__contains=area
    ).all()
    