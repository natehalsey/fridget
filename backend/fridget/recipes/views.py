from fastapi import APIRouter, HTTPException, Response
from fridget.recipes.models import RecipeModel
from fridget.base.schema import Recipe
from fridget.recipes.models import RecipeModel, RecipeName
from fridget.users.models import UserRecipeModel
from fridget.recipes.controller import RecipeController

    
router = APIRouter(
    prefix = "/recipes"
)

recipe_controller = RecipeController()

@router.post("/get-recipes-by-name")
async def get_recipes_by_name(recipe_name: RecipeName) -> list[Recipe]:
    return await recipe_controller.filter_recipe_by_name(recipe_name.name)

@router.get("/get-recipes-by-id")
async def get_recipes_by_id(recipe_id: int) -> Recipe:
    return await recipe_controller.filter_recipe_by_id(recipe_id)

@router.post("/create-recipe")
async def create_recipe(user_recipe: UserRecipeModel):
    
    try:
        await recipe_controller.create_recipe(user_recipe)
        
    except TypeError as e:
        raise HTTPException(status_code=400, detail=e)
    
    return Response(status_code=200)
    
    
    


    
