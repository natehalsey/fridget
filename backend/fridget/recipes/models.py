from pydantic import BaseModel
from typing import Optional
from fridget.ingredients.models import IngredientMeasurementModel

class AreaModel(BaseModel):
    name: str

class CategoryModel(BaseModel):
    name: str

class RecipeModel(BaseModel):
    id: Optional[str]
    name: Optional[str]
    category: Optional[CategoryModel]
    area: Optional[AreaModel]
    instructions: Optional[str]
    ingredients_measurements: Optional[list[IngredientMeasurementModel]]
    image_url: Optional[str]
    source: Optional[str]
    
