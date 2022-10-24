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

    pass
