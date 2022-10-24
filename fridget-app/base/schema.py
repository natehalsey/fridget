from datetime import datetime
from typing import Optional
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



class Recipe(ormar.Model):
    
    class Meta(BaseMeta):
        tablename="recipe"

    id: int = ormar.Integer(primary_key=True)       
    name: str = ormar.String(max_length=20)

