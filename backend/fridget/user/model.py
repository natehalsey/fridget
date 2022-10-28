

from typing import Optional, List
from ormar import Model, Integer, String, ManyToMany
from ..receipe.model import Recipe
from ..base.schema import BaseMeta

class Users(Model):

    class Meta(BaseMeta):
        tablename="users"

    id: int = Integer(primary_key=True)
    username: str = String(max_length=20)
    hashed_password: str = String(max_length=200)
    my_recipes: Optional[List[Recipe]] = ManyToMany(Recipe)
    saved_recipes: Optional[List[Recipe]] = ManyToMany(Recipe)