import ormar
from fastapi import APIRouter
from fridget.categories.models import CategoryModel
from fridget.base.schema import Category


router = APIRouter(
    prefix = "/categories"
)

@router.get("/get-all-categories")
async def get_categories():
    return await Category.objects.select_related("recipes").all()


@router.get("/get-recipes-by-category")
async def get_recipes_by_category(category_model: CategoryModel):
    try:
        recipes = await Category.objects.select_related("recipes").get(
            name=category_model.name
        )
    except ormar.NoMatch:
        return None
    
    return recipes
    