import ormar
from fastapi import APIRouter, Response
from fridget.users.models import LoginRequestModel, SaveRecipeModel, UserIngredientModel
from fridget.base.schema import User, Recipe, Ingredient
from fridget.ingredients.models import IngredientListModel


router = APIRouter(
    prefix = "/users"
)

@router.post('/login')
async def login(user_info: LoginRequestModel) -> User:
    user, _ = await User.objects.get_or_create(
        given_name=user_info.given_name,
        family_name=user_info.family_name,
        picture=user_info.picture,
        email=user_info.email
    )
    return user

@router.post("/add-ingredients")
async def add_user_ingredients(user_ingredients: UserIngredientModel) -> Response:
    try:
        user = await User.objects.get(
            id=user_ingredients.user_id
        )
    except ormar.NoMatch:
        return Response(status_code=404, detail="Not found")
    
    for ingredient in user_ingredients.ingredients:
        ingredient, _ = await Ingredient.objects.get_or_create(name=ingredient)
        await user.ingredients.add(ingredient)
    
    return Response(status_code=200)

@router.get("/get-ingredients")
async def get_user_ingredients(user_id: int) -> IngredientListModel:
    try:
        user = await User.objects.select_related("ingredients").get(
            id=user_id
        )
    except ormar.NoMatch:
        return Response(status_code=404, detail="Not found")

    return IngredientListModel(
        ingredients=[ingredient.name for ingredient in user.ingredients]
    )
        
@router.get("/get-saved-recipes")
async def get_saved_recipes(user_id: int) -> list[Recipe]:
    
    try:
        user = await User.objects.select_related("saved_recipes").get(
            id=user_id
        )
    
    except ormar.NoMatch:
        return Response(status_code=404, detail="Not found")
    
    return user.saved_recipes
    
@router.get("/get-created-recipes")
async def get_created_recipes(user_id: int) -> list[Recipe]:
    
    try:
        user =  await User.objects.select_related("created_recipes").get(
            id=user_id
        )
    except ormar.NoMatch:
        return Response(status_code=404, detail="Not found")
    
    return user.created_recipes

@router.post("/save-recipe")
async def save_recipe(save_recipe: SaveRecipeModel) -> Response:
    try:
        recipe = await Recipe.objects.get(
            id=save_recipe.recipe_id
        )
        user = await User.objects.get(
            id=save_recipe.user_id
        )
        await user.saved_recipes.add(recipe)
        
        return Response(status_code=200)
        
    except ormar.NoMatch:
        return Response(status_code=404, detail="Not found")

# debugging only, remove before prod
@router.get("/get-users")
async def get_users() -> list[User]:
    return await User.objects.select_related("created_recipes").all()

