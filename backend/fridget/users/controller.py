import ormar
from fastapi import Response
from fridget.base.schema import User, Ingredient, Recipe
from fridget.users.models import LoginRequestModel, UserIngredientModel, SaveRecipeModel
from fridget.ingredients.models import IngredientListModel

class UserController:


    async def login(user_info: LoginRequestModel) -> User:
        user, _ = await User.objects.get_or_create(
            given_name=user_info.given_name,
            family_name=user_info.family_name,
            picture=user_info.picture,
            email=user_info.email
        )
        return user

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
            
    async def get_saved_recipes(user_id: int) -> list[Recipe]:
        
        try:
            user = await User.objects.select_related("saved_recipes").get(
                id=user_id
            )
        
        except ormar.NoMatch:
            return Response(status_code=404, detail="Not found")
        
        return user.saved_recipes
        
    async def get_created_recipes(user_id: int) -> list[Recipe]:
        
        try:
            user =  await User.objects.select_related("created_recipes").get(
                id=user_id
            )
        except ormar.NoMatch:
            return Response(status_code=404, detail="Not found")
        
        return user.created_recipes

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
    async def get_users() -> list[User]:
        return await User.objects.select_related("created_recipes").all()