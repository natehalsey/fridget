from fastapi import APIRouter

from fridget.base.schema import Category


router = APIRouter(
    prefix = "/categories"
)

@router.get("/get-recipes-by-category")
async def get_recipes_by_category(category: str):
    return await Category.objects.select_related("recipes").filter(
        name__contains=category
    ).all()

