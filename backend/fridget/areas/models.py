from pydantic import BaseModel

class AreaModel(BaseModel):
    name: str
    
class AreaListModel(BaseModel):
    areas: list[str]