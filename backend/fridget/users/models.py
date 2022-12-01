from pydantic import BaseModel
from fridget.recipes.models import RecipeModel


# Models associated with user response
class UserModel(BaseModel):
    username: str
    ingredients: list[str]
    created_recipes: list[RecipeModel]
    saved_recipes: list[RecipeModel]
