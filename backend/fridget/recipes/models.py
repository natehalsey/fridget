from pydantic import BaseModel
from typing import Optional
from fridget.ingredients.models import IngredientMeasurementModel
from fridget.areas.models import AreaModel
from fridget.categories.models import CategoryModel

class RecipeModel(BaseModel):

    name: str
    category: Optional[CategoryModel]
    area: Optional[AreaModel]
    instructions: Optional[str]
    ingredients_measurements: Optional[list[IngredientMeasurementModel]]
    image_url: Optional[str]
    source: Optional[str]
    
