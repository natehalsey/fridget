import sqlalchemy
import databases
import ormar

DATABASE_URL = "sqlite:///db.sqlite"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Recipes(ormar.Model):
    
    class Meta(BaseMeta):
        tablename="recipes"

    pass
