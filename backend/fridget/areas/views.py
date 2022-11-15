from fastapi import APIRouter
from fridget.base.schema import Area


router = APIRouter(
    prefix = "/areas"
)
@router.get("/get-recipes-by-area")
async def get_recipes_by_area(area: str):
    return await Area.objects.select_related("recipes").filter(
        name__icontains=area
    ).all()