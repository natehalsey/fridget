from pydantic import BaseModel


class LoginRequestModel(BaseModel):
    given_name: str
    family_name: str
    picture: str
    email: str
