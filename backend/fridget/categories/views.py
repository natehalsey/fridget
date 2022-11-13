import ormar
from fastapi import APIRouter
from fridget.categories.models import CategoryModel, CategoryListModel
from fridget.base.schema import Category


router = APIRouter(
    prefix = "/categories"
)

@router.get("/get-recipes-by-category")
async def get_recipes_by_category(category_list_model: CategoryListModel):
    try:
        recipes = await Category.objects.select_related("recipes").get(
            name__in=category_list_model.categories
        )
    except ormar.NoMatch:
        return None
    
    return recipes
    