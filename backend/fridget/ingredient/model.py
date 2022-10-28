from ormar import Model, Integer, String
from ..base.schema import BaseMeta, Label


class Ingredient(Label):

    class Meta(BaseMeta):
        tablename="Ingredient"

    measure: str = String(max_length=20)