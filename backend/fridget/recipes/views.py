from fastapi import APIRouter, HTTPException, Response
from fridget.recipes.models import RecipeModel
from fridget.base.schema import Recipe
from fridget.recipes.models import RecipeModel
from fridget.users.models import UserRecipeModel
from fridget.recipes.controller import RecipeController

    
router = APIRouter(
    prefix = "/recipes"
)

recipe_controller = RecipeController()

@router.get("/get-recipes-by-name")
async def get_recipes_by_name(name: str) -> list[Recipe]:
    return await recipe_controller.filter_recipe_by_name(name)

@router.post("/create-recipe")
async def create_recipe(user_recipe: UserRecipeModel):
    
    try:
        await recipe_controller.create_recipe(user_recipe)
        
    except TypeError as e:
        raise HTTPException(status_code=400, detail=e)
    
    return Response(status_code=200)
    
    
    


    
