from pydantic import BaseModel, Field

class Recipe(BaseModel):
    name: str