from pydantic import BaseModel

class MeasurementModel(BaseModel):
    measurement: str

class IngredientModel(BaseModel):
    name: str
    description: str
    type: str
    
class IngredientMeasurementModel(BaseModel):
    ingredient: str
    measurement: str
    
class IngredientListModel(BaseModel):
    ingredients: list[str]
