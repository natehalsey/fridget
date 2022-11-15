from fastapi import APIRouter
from fridget.areas.models import AreaListModel
from fridget.base.schema import Area


router = APIRouter(
    prefix = "/areas"
)
@router.post("/get-recipes-by-area")
async def get_recipes_by_area(area_list_model: AreaListModel):
    return await Area.objects.select_related("recipes").filter(
        name__icontains=area_list_model.areas[0]
    ).all()