import operator
from collections import Counter
from fridget.base.schema import Ingredient
from fridget.recipes.models import RecipeModel

class IngredientController:
        
    async def get_recipes_by_ingredients(self, input_ingredients: list[str]) -> list[RecipeModel]:
        
        recipes = [
            recipes for ingredient_name in input_ingredients for recipe in
            await Ingredient.objects.select_related("recipes").filter(
                name__iexact=ingredient_name
            ).all()
            for recipes in recipe.recipes
        ]
        counts = Counter([recipe.id for recipe in recipes])
        sorted_recipes = sorted(
            recipes,
            key=lambda recipe: counts[recipe.id],
            reverse=True
        )
        return sorted_recipes
        