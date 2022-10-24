from pydantic import BaseModel, Field

class Ingredients(BaseModel):
    name: str
    measure: str