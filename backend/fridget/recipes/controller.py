
from fridget.base.schema import Recipe, Ingredient, Measurement, RecipeIngredientMeasurement
from fridget.ingredients.models import IngredientMeasurementModel
from fridget.recipes.models import RecipeModel

class RecipeController:

    async def create_recipe(self, recipe_model: RecipeModel):
        ingredients_measurements = await self._parse_ingredients(recipe_model)
        recipe = await Recipe.objects.create(
            **recipe_model.dict()
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
        
    async def filter_recipe_by_name(self, recipe_model: RecipeModel) -> list[Recipe]:
        return await Recipe.objects.filter(
            name__contains=recipe_model.name
        ).all()
        
    async def get_all_recipes(self) -> list[Recipe]:
        return await Recipe.objects.select_related(
            "area"
        ).select_related("category").all()
        

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