from pydantic import parse_obj_as
from .models import Recipe
from typing import List

class RequestRecipe():
    def request_recipe(self, query) -> Recipe:
        
        pass
    
    def paginated_recipes(self, query) -> List[Recipe]:
        
        pass