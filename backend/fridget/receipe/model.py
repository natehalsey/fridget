
from typing import Optional, List
from ormar import Model, Integer, String, ForeignKey, ManyToMany
from ..ingredient.model import Ingredient
from ..area.model import Area
from ..category.model import Category
from ..user.model import User

class Recipe(Model):     

    class Meta(Recipe):
        tablename="users"

    id: int = Integer(primary_key=True)
    name: str = String(max_length=200)
    category: Category = ForeignKey(Category)
    area: Area = ForeignKey(Area)
    instructions: str = String(max_length=3000)
    image_url: str = String(max_length=200)
    youtube_url: Optional[str]  = String(max_length=100)
    ingredients: List[Ingredient] = ManyToMany(Ingredient)
    created_by: User = ManyToMany(User) # either its User created or from TheMealDb API (a type of "user")