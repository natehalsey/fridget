from pydantic import BaseModel, Field
from typing import Optional, List
from ..ingredients.models import Ingredients

class Recipes(BaseModel):     
    name: str
    category: str
    area: str
    instructions: str
    image_url: str
    youtube_url: Optional[str]
    ingredients: List[Ingredients]