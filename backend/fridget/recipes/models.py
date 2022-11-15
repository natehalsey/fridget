from pydantic import BaseModel
from typing import Optional
from fridget.ingredients.models import IngredientMeasurementModel

class AreaModel(BaseModel):
    name: str

class CategoryModel(BaseModel):
    name: str

class RecipeModel(BaseModel):
    id: Optional[int]
    name: Optional[str]
    category: Optional[CategoryModel]
    area: Optional[AreaModel]
    instructions: Optional[str]
    ingredients_measurements: Optional[list[IngredientMeasurementModel]]
    image_url: Optional[str]
    source: Optional[str]
    
class AreaRecipesModel(BaseModel):
    name: str # name of the area 
    recipes: list[RecipeModel] # list of recipes matching area

class CategoryRecipesModel(BaseModel):
    name: str # name of the category
    recipes: list[RecipeModel] # list of recipes matching category