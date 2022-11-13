import ormar
from fastapi import APIRouter, Response
from .models import LoginRequestModel, SaveRecipeModel
from fridget.base.schema import User, Recipe


router = APIRouter(
    prefix = "/users"
)

@router.post('/login')
async def login(user_info: LoginRequestModel):
    user, _ = await User.objects.get_or_create(
        given_name= user_info.given_name,
        family_name= user_info.family_name,
        picture= user_info.picture,
        email= user_info.email
    )
    return user

@router.get("/get-saved-recipes")
async def get_saved_recipes(user_id: int):
    return await Recipe.objects.filter(
        saved_by__id=user_id
    ).all()
    
@router.get("/get-created-recipes")
async def get_created_recipes(user_id: int):
    return await Recipe.objects.filter(
        created_by__id=user_id
    ).all()

@router.post("/save-recipe")
async def save_recipe(save_recipe: SaveRecipeModel):
    try:
        recipe = await Recipe.objects.get(
            id=save_recipe.recipe_id
        )
        user = await User.objects.get(
            id=save_recipe.user_id
        )
        await recipe.saved_by.add(user)
        
        return Response(status_code=200)
        
    except ormar.NoMatch as e:
        return Response(status_code=404, detail="Not found")

# debugging only, remove before prod
@router.get("/get-users")
async def get_users():
    return await User.objects.select_related("created_recipes").all()

