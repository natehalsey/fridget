import ormar
from random import randint
from fastapi import Response
from fridget.base.schema import (
    Area, 
    Category, 
    Ingredient, 
    Recipe, 
    User,
    UserCreatedRecipe,
)
from fridget.ingredients.models import IngredientMeasurementModel
from fridget.recipes.models import RecipeModel
from fridget.users.models import UserRecipeModel

class RecipeController:

    async def create_recipe(self, recipe_model: UserRecipeModel) -> None:
        
        area, _ = await Area.objects.get_or_create(
            name=recipe_model.recipe.area.name
        )
        category, _ = await Category.objects.get_or_create(
            name=recipe_model.recipe.category.name
        )
        
        try:
            user = await User.objects.get(
                id=recipe_model.user_id
            )
        except ormar.NoMatch:
            return Response(status_code=404, detail="Not found")
            
        recipe = await Recipe.objects.create(
            name=recipe_model.recipe.name,
            category=category,
            area=area,
            instructions=recipe_model.recipe.instructions,
            ingredients_measurements=recipe_model.recipe.dict()["ingredients_measurements"],
            image_url=recipe_model.recipe.image_url,
            source=recipe_model.recipe.source,
        )
        
        await UserCreatedRecipe.objects.create(
            user=user,
            recipe=recipe
        )
        ingredients_measurements: list[IngredientMeasurementModel] = recipe_model.recipe.ingredients_measurements

            
        for ingredient_measurement in ingredients_measurements:
            
            ingredient, _ = await Ingredient.objects.get_or_create(
                name=ingredient_measurement.ingredient
            )
            await recipe.ingredients.add(ingredient)  
        
        
    async def get_recipes_by_name(self, name: str) -> list[Recipe]:
        return await Recipe.objects.filter(
            name__icontains=name
        ).all()

    async def get_recipe_by_id(self, id: int) -> Recipe:
        try:
            return await Recipe.objects.get(
                id=id
            )
        except ormar.NoMatch:
            return Response(status_code=404, detail="Not found")

    async def get_recipes_by_random(self, n: int) -> Recipe:
        random_offset = randint(0, await Recipe.objects.count() - n)
        return await Recipe.objects.offset(random_offset).limit(n).all()
        