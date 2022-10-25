import sqlalchemy
import databases
import ormar

DATABASE_URL = "sqlite:///db.sqlite"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Users(ormar.Model):

    class Meta(BaseMeta):
        tablename="users"

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=20)
    hashed_password: str = ormar.String(max_length=200)
