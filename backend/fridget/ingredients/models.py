from pydantic import BaseModel

class MeasurementModel(BaseModel):
    measurement: str

class IngredientModel(BaseModel):
    name: str
    description: str
    type: str
    

class IngredientMeasurementModel(BaseModel):
    ingredient: IngredientModel
    measurement: MeasurementModel
    

