from pydantic import BaseModel, Field

class Ingredient(BaseModel):
    name: str