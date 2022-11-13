from pydantic import BaseModel
from fridget.recipes.models import RecipeModel

class LoginRequestModel(BaseModel):
    given_name: str
    family_name: str
    picture: str
    email: str


class UserRecipeModel(BaseModel):
    user_id: int
    recipe: RecipeModel
    
class SaveRecipeModel(BaseModel):
    user_id: int
    recipe_id: int