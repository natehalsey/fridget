from pydantic import BaseModel
from typing import Optional

class AreaModel(BaseModel):
    name: str

class CategoryModel(BaseModel):
    name: str
    
class IngredientMeasurementModel(BaseModel):
    ingredient: str
    measurement: str

class IngredientListModel(BaseModel):
    ingredients: list[str]

class RecipeModel(BaseModel):
    id: Optional[str]
    name: Optional[str]
    category: Optional[CategoryModel]
    area: Optional[AreaModel]
    instructions: Optional[str]
    ingredients_measurements: Optional[list[IngredientMeasurementModel]]
    image_url: Optional[str]
    source: Optional[str]
    
