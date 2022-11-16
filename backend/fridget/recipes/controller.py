import ormar
from fastapi import Response
from fridget.base.schema import Recipe, Ingredient, Measurement, RecipeIngredientMeasurement, Area, Category, User
from fridget.ingredients.models import IngredientMeasurementModel
from fridget.recipes.models import RecipeModel
from fridget.users.models import UserRecipeModel

class RecipeController:

    async def create_recipe(self, recipe_model: UserRecipeModel) -> None:
        ingredients_measurements = await self._parse_ingredients(recipe_model.recipe)
        
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
            return Response(status_code=403)
            
        recipe = await Recipe.objects.create(
            name=recipe_model.recipe.name,
            category=category,
            area=area,
            instructions=recipe_model.recipe.instructions,
            ingredients_measurements=recipe_model.recipe.dict()["ingredients_measurements"],
            image_url=recipe_model.recipe.image_url,
            source=recipe_model.recipe.source,
            created_by=user
        )
        
        recipes_ingredients_measurements: list[RecipeIngredientMeasurement] = []
        
        for ingredient_measurement in ingredients_measurements:
            
            ingredient, measurement = ingredient_measurement
            
            recipes_ingredients_measurements.append(
                RecipeIngredientMeasurement(
                    ingredient=ingredient,
                    measurement=measurement,
                    recipe=recipe
                )
            )
                        
        await RecipeIngredientMeasurement.objects.bulk_create(
            recipes_ingredients_measurements
        )
        
    async def filter_recipe_by_name(self, name: str) -> list[Recipe]:
        return await Recipe.objects.filter(
            name__icontains=name
        ).all()

    async def filter_recipe_by_id(self, id: int) -> Recipe:
        return await Recipe.objects.get(
            id=id
        )
        
    async def _parse_ingredients(self, recipe_model: RecipeModel) -> list[tuple[Ingredient, Measurement]]:
            ingredients_measurements: list[IngredientMeasurementModel] = recipe_model.ingredients_measurements
            

            ingredients: list[tuple[Ingredient, Measurement]] = []
            
            for ingredient_measurement in ingredients_measurements:
                
                ingredient, _ = await Ingredient.objects.get_or_create(
                    name=ingredient_measurement.ingredient
                )
                
                measurement, _ = await Measurement.objects.get_or_create(
                    measurement=ingredient_measurement.measurement
                )
                ingredients.append((ingredient,measurement))
            
            return ingredients