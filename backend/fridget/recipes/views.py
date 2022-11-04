from fastapi import APIRouter, HTTPException, Response
from fridget.recipes.models import RecipeModel
from fridget.base.schema import Recipe
from fridget.recipes.models import RecipeModel
from fridget.recipes.controller import RecipeController

    
router = APIRouter(
    prefix = "/recipes"
)

recipe_controller = RecipeController()

@router.get("/get-recipes")
async def get_recipes() -> list[Recipe]:
    return await recipe_controller.get_all_recipes()

@router.get("/get-recipes-by-name")
async def get_recipes_by_name(recipe_model: RecipeModel) -> list[Recipe]:
    
    return await recipe_controller.filter_recipe_by_name(recipe_model)

@router.post("/create-recipe")
async def create_recipe(recipe: RecipeModel):
    
    try:
        await recipe_controller.create_recipe(recipe)
        
    except TypeError as e:
        raise HTTPException(status_code=400, detail=e)
    
    return Response(status_code=200)
    
    
    


    
