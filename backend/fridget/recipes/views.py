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
    """
    This function returns a list of RecipeModel matched by recipe name

    :param name: str
    :type name: str
    :return: A list of RecipeModel objects
    """
    return await recipe_controller.get_recipes_by_name(name)


@router.get("/get-recipe-by-id", response_model=RecipeModel)
async def get_recipe_by_id(id: int) -> RecipeModel:
    """
    This function returns a recipe by its id

    :param id: int - The id of the recipe you want to get
    :type id: int
    :return: A RecipeModel object
    """
    return await recipe_controller.get_recipe_by_id(id)


@router.get("/get-recipes-by-random", response_model=list[RecipeModel])
async def get_recipes_by_random(n: int) -> list[RecipeModel]:
    """
    "Get a list of n random recipes."

    :param n: int
    :type n: int
    :return: A list of RecipeModel objects
    """
    return await recipe_controller.get_recipes_by_random(n)


@router.post("/create-recipe")
async def create_recipe(recipe_model: RecipeModel, current_user: User = Depends(get_current_active_user)):
    """
    Creates a new recipe

    :param recipe_model: RecipeModel - this is the model that we created earlier
    :type recipe_model: RecipeModel
    :param current_user: User = Depends(get_current_active_user)
    :type current_user: User
    :return: The response is being returned.
    """

    await recipe_controller.create_recipe(recipe_model, current_user)
    return Response(status_code=200)


@router.get("/get-recipes-by-category", response_model=list[RecipeModel])
async def get_recipes_by_category(category: str) -> list[RecipeModel]:
    """
    "Get all recipes by the given category name."

    :param category: str
    :type category: str
    :return: A list of RecipeModel objects
    """
    return await Recipe.objects.filter(
        category__name__icontains=category
    ).all()


@router.get("/get-recipes-by-ingredients", response_model=list[RecipeModel])
async def get_recipes_by_ingredients(ingredients: str) -> list[RecipeModel]:
    """
    It takes a comma-separated list of ingredients, and returns a list of recipes that contain those
    ingredients

    :param ingredients: str
    :type ingredients: str
    :return: A list of RecipeModel objects
    """
    return await recipe_controller.get_recipes_by_ingredients(ingredients.split(","))


@router.get("/get-recipes-by-area", response_model=list[RecipeModel])
async def get_recipes_by_area(area: str) -> list[RecipeModel]:
    """
    "Get all recipes by the given area."

    :param area: str
    :type area: str
    :return: A list of RecipeModel objects
    """
    return await Recipe.objects.filter(
        area__name__icontains=area
    ).all()
