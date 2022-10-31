import ormar
from fastapi import APIRouter
from fridget.areas.models import AreaModel
from fridget.base.schema import Area


router = APIRouter(
    prefix = "/areas"
)

@router.get("/get-areas")
async def get_areas():
    return await Area.objects.select_related("recipes").all()

@router.get("/get-recipes-by-area")
async def get_recipes_by_area(area_model: AreaModel):
    try:
        recipes = await Area.objects.select_related("recipes").get(
            name=area_model.name
        )
    except ormar.NoMatch:
        return None
    
    return recipes
