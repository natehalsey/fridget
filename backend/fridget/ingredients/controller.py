from fridget.base.schema import Ingredient, RecipeIngredientMeasurement
from fridget.ingredients.models import IngredientModel, IngredientListModel

class IngredientController:
    async def get_all_ingredients(self) -> list[Ingredient]:
        return await Ingredient.objects.all()
        
    async def create_ingredient(self, ingredient_model: IngredientModel) -> None:
        await Ingredient.objects.create(
            name=ingredient_model.name,
            description=ingredient_model.description,
            type=ingredient_model.type
        )
    
    async def search_by_ingredients(self, ingredients: IngredientListModel) -> list[RecipeIngredientMeasurement]:
        return await RecipeIngredientMeasurement.objects.select_related("ingredient").filter(
            ingredient__name__in=ingredients.ingredients
        ).select_related("recipe").all()