import ormar
from fastapi import APIRouter
from fridget.areas.models import AreaListModel
from fridget.base.schema import Area


router = APIRouter(
    prefix = "/areas"
)

@router.get("/get-areas")
async def get_areas():
    return await Area.objects.select_related("recipes").all()

@router.get("/get-recipes-by-area")
async def get_recipes_by_area(area_list_model: AreaListModel):
    print(area_list_model)
    return await Area.objects.select_related("recipes").filter(
        name__in=area_list_model.areas
    ).all()