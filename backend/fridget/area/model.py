from ormar import Model, Integer, String
from ..base.schema import BaseMeta


class Area(Model):

    class Meta(BaseMeta):
        tablename="Area"

    id: int = Integer(primary_key=True)
    name: str = String(max_length=20)