from fastapi import APIRouter
from fridget.recipes.models import RecipeModel, CategoryRecipesModel

from fridget.base.schema import Category


router = APIRouter(
    prefix = "/categories"
)

@router.get("/get-recipes-by-category")
async def get_recipes_by_category(category: str) -> list[RecipeModel]:
    categories: list[CategoryRecipesModel] = await Category.objects.select_related("recipes").filter(
        name__contains=category
    ).all()

    return [recipe for category in categories for recipe in category.recipes]
