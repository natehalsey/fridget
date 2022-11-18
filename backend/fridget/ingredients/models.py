from pydantic import BaseModel
from typing import Optional


class IngredientModel(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    type: Optional[str]
    
class IngredientMeasurementModel(BaseModel):
    ingredient: str
    measurement: str

class IngredientListModel(BaseModel):
    ingredients: list[str]