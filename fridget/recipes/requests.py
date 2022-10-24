import httpx
from pydantic import parse_obj_as
from .models import Recipes
from typing import List
from  ..config import Settings

class RequestRecipes():
    def search_recipes_by_name(self, name: str):
        name = name.replace(" ", "_") # all spaces become underscores
        with httpx.Client(headers=Settings.RECIPE_HEADERS) as client:
            r = client.get(Settings.RECIPE_API_URL+f"/search.php?s="+name)

        return r.json()
    
    def search_recipes_by_category(self, category: str):
        category = category.replace(" ", "_") # all spaces become underscores
        with httpx.Client(headers=Settings.RECIPE_HEADERS) as client:
            r = client.get(Settings.RECIPE_API_URL+f"/search.php?c="+category)

        return r.json()
    
