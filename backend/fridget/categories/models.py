from pydantic import BaseModel

class CategoryModel(BaseModel):
    name: str

class CategoryListModel(BaseModel):
    categories: list[str]