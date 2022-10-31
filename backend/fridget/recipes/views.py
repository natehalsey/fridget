import ormar
from fastapi import APIRouter, HTTPException
from fridget.recipes.models import RecipeModel
from fridget.base.schema import Recipe
from fridget.recipes.models import RecipeModel

router = APIRouter(
    prefix = "/recipes"
)
    
@router.get("/get-recipes")
async def get_recipes():
    return await Recipe.objects.select_all().all()

@router.get("/get-recipes-by-name")
async def get_recipes_by_name(recipe_model: RecipeModel):
    recipe = await Recipe.objects.filter(
        name__contains=recipe_model.name
    ).all()

    return recipe

@router.post("/create-recipe")
async def create_recipe(recipe: RecipeModel):
    try:
        new_recipe = Recipe(**recipe.dict())
        
    except TypeError as e:
        raise HTTPException(status_code=400, detail=e)
    
    
    return new_recipe
    
    
    


    
