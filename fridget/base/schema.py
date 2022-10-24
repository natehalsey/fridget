from datetime import datetime
from typing import Optional, List
from ..ingredients.models import Ingredients
import sqlalchemy
import databases
import ormar

from ..config import Settings

DATABASE_URL = Settings.DATABASE

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database



class Recipes(ormar.Model):
    
    class Meta(BaseMeta):
        tablename="recipes"

    id: int = ormar.Integer(primary_key=True)       
    name: str = ormar.String(max_length=20)
    category: str = ormar.String(max_length=20)
    area: str = ormar.String(max_length=20)
    instructions: str = ormar.String(max_length=5000)
    image_url: str = ormar.String(max_length=100)
    youtube_url: Optional[str] = ormar.String(max_length=100)
    ingredients: str = ormar.JSON()

class Users(ormar.Model):
    
    class Meta(BaseMeta):
        tablename="users"
    
    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=20)
    hashed_password: str = ormar.String(max_length=200)
    

class Links(ormar.Model):
    class Meta(BaseMeta):
        tablename="links"
    
    id: int = ormar.Integer(primary_key=True)
    recipe: int = ormar.Integer()
    user: int = ormar.Integer()