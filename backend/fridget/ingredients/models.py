from pydantic import BaseModel
from typing import Optional

class MeasurementModel(BaseModel):
    id: int
    measurement: str

class IngredientModel(BaseModel):
    id: int
    name: str
    description: Optional[str]
    type: Optional[str]
    
class IngredientMeasurementModel(BaseModel):
    ingredient: str
    measurement: str
    
class IngredientListModel(BaseModel):
    ingredients: list[str]
