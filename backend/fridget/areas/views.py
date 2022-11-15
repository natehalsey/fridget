from fastapi import APIRouter
from fridget.base.schema import Area
from fridget.recipes.models import RecipeModel, AreaRecipesModel

router = APIRouter(
    prefix = "/areas"
)
@router.get("/get-recipes-by-area")
async def get_recipes_by_area(area: str) -> list[RecipeModel]:
    areas: list[AreaRecipesModel] = await Area.objects.select_related("recipes").filter(
        name__contains=area
    ).all()
    
    return [recipe for area in areas for recipe in area.recipes]
