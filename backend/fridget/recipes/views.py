from fastapi import APIRouter, Response, Depends
from fridget.base.schema import Recipe, User
from fridget.recipes.models import RecipeModel
from fridget.recipes.controller import RecipeController
from fridget.base.auth.auth import get_current_active_user


router = APIRouter(
    prefix="/recipes"
)


recipe_controller = RecipeController()

# this file contains views that anybody can access without authentication,
# non user specific items


@router.get("/get-recipes-by-name", response_model=list[RecipeModel])
async def get_recipes_by_name(name: str) -> list[RecipeModel]:
    return await recipe_controller.get_recipes_by_name(name)


@router.get("/get-recipe-by-id", response_model=RecipeModel)
async def get_recipe_by_id(id: int) -> RecipeModel:
    return await recipe_controller.get_recipe_by_id(id)


@router.get("/get-recipes-by-random", response_model=list[RecipeModel])
async def get_recipes_by_random(n: int) -> list[RecipeModel]:
    return await recipe_controller.get_recipes_by_random(n)


@router.post("/create-recipe")
async def create_recipe(recipe_model: RecipeModel, current_user: User = Depends(get_current_active_user)):
    await recipe_controller.create_recipe(recipe_model, current_user)
    return Response(status_code=200)


@router.get("/get-recipes-by-category", response_model=list[RecipeModel])
async def get_recipes_by_category(category: str) -> list[RecipeModel]:
    return await Recipe.objects.filter(
        category__name__icontains=category
    ).all()


@router.get("/get-recipes-by-ingredients", response_model=list[RecipeModel])
async def get_recipes_by_ingredients(ingredients: str) -> list[RecipeModel]:
    return await recipe_controller.get_recipes_by_ingredients(ingredients.split(","))


@router.get("/get-recipes-by-area", response_model=list[RecipeModel])
async def get_recipes_by_area(area: str) -> list[RecipeModel]:
    return await Recipe.objects.filter(
        area__name__icontains=area
    ).all()
