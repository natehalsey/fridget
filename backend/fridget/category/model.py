from __future__ import annotations

from ormar import Model, Integer, String
from fridget.base.schema import BaseMeta, Label
from typing import List
from pydantic import BaseModel

## Ormar DB Models

class Category(Label):

    class Meta(BaseMeta):
        tablename="Category"



## Pydantic API Models

class Meal(BaseModel):
    strCategory: str


class APIResponseModel(BaseModel):
    meals: List[Meal]