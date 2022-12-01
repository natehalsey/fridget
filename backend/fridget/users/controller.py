import ormar
from fastapi import status, HTTPException, Response
from fridget.recipes.models import IngredientListModel
from fridget.base.schema import Recipe, User, UserSavedRecipe, UserCreatedRecipe, Ingredient, UserIngredient


# user controller controls all user actions
class UserController:
    async def add_user_ingredient(self, ingredient: str, current_user: User):
        ingredient, _ = await Ingredient.objects.get_or_create(name=ingredient)
        await UserIngredient.objects.create(
            user=current_user,
            ingredient=ingredient
        )        
        return Response(status_code=status.HTTP_201_CREATED)

    async def remove_ingredient(self, ingredient: str, current_user: User):
        ingredient = await Ingredient.objects.get(
            name=ingredient
        )
        await UserIngredient.objects.delete(
            user=current_user,
            ingredient=ingredient
        )
        return Response(status_code=status.HTTP_200_OK)
        
    
    async def get_user_ingredients(self, current_user: User) -> IngredientListModel:
        user_ingredients = await UserIngredient.objects.select_related("ingredient").fields("ingredient").filter(
            user=current_user
        ).all()
        
        return IngredientListModel(
            ingredients=[
                user_ingredient.ingredient.name 
                for user_ingredient in user_ingredients
            ]
        )
    
    async def get_saved_recipes(self, current_user: User):
        user_saved_recipes = await UserSavedRecipe.objects.select_related("recipe").filter(
            user=current_user
        ).all()
        return [user_saved_recipe.recipe for user_saved_recipe in user_saved_recipes]
    
    
    async def get_created_recipes(self, current_user: User):
        user_created_recipes = await UserCreatedRecipe.objects.select_related("recipe").filter(
            user=current_user
        ).all()
        return [user_created_recipe.recipe for user_created_recipe in user_created_recipes]
    
    async def save_recipe(self, recipe_id: int, current_user: User):
        try:
            recipe = await Recipe.objects.get(
                id=recipe_id
            )
        except ormar.NoMatch:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        
        await UserSavedRecipe.objects.create(
            user=current_user,
            recipe=recipe,
        )
        return Response(status_code=status.HTTP_200_OK)
    
    async def remove_saved_recipe(self, recipe_id: int, current_user: User):
        try:
            recipe = await Recipe.objects.get(
                id=recipe_id
            )
        except ormar.NoMatch:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        
        await UserSavedRecipe.objects.delete(
            user=current_user,
            recipe=recipe,
        )
        return Response(status_code=status.HTTP_200_OK)
    
    async def remove_created_recipe(self, recipe_id: int, current_user: User):
        try:
            recipe = await Recipe.objects.get(
                id=recipe_id
            )
        except ormar.NoMatch:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        
        try:
            user_created_recipe = await UserCreatedRecipe.objects.get(
                user=current_user,
                recipe=recipe,
        )
            
        except ormar.NoMatch:
            raise HTTPException(status_code=status.HTTP_401_NOT_AUTHORIZED, detail="Not authorized")
        
        await user_created_recipe.delete()
        
        await UserSavedRecipe.objects.delete(
            recipe=recipe
        )
        await recipe.delete()
        
        return Response(status_code=status.HTTP_200_OK)