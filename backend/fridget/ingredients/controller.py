import operator
from collections import defaultdict
from fridget.base.schema import Ingredient, RecipeIngredientMeasurement
from fridget.ingredients.models import IngredientModel, IngredientListModel
from fridget.recipes.models import RecipeModel

class IngredientController:
        
    async def get_recipes_by_ingredients(self, ingredients: IngredientListModel) -> list[RecipeModel]:
        recipes = await RecipeIngredientMeasurement.objects.select_related("ingredient").filter(
            ingredient__name__in=ingredients.ingredients
        ).select_related("recipe").all()
        
        recipe_ingredients: dict[RecipeModel, list[str]] = defaultdict(list)
        recipe_id_recipe: dict[str, RecipeModel] = {}
        
        
        for recipe in recipes:

            recipe_ingredients[recipe.recipe.id].append(recipe.ingredient.name)
            recipe_id_recipe[recipe.recipe.id] = RecipeModel.parse_obj(recipe.recipe)
    
        sorted_recipes = self._sort_dict_by_list_len(recipe_ingredients)
        return [recipe_id_recipe[sorted_recipe] for sorted_recipe in sorted_recipes]
        
    
    def _sort_dict_by_list_len(self, dictionary_with_list: dict[RecipeModel, list[str]]) -> dict[RecipeModel, list[str]]:
        dict_len: dict[str,str] = {key: len(value) for key, value in dictionary_with_list.items()}
        sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=True)
        sorted_dict = {item[0]: dictionary_with_list[item [0]] for item in sorted_key_list}
        
        return list(sorted_dict.keys())
        