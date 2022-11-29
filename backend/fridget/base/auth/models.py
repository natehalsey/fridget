from pydantic import BaseModel
from fastapi.param_functions import Form
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    
    
class OAuth2EmailPasswordRequestForm:

    def __init__(
        self,
        grant_type: str = Form(default=None, regex="password"),
        username: str = Form(),
        email: str = Form(),
        password: str = Form(),
        scope: str = Form(default=""),
        client_id: Optional[str] = Form(default=None),
        client_secret: Optional[str] = Form(default=None),
    ):
        self.grant_type = grant_type
        self.username = username
        self.email = email
        self.password = password
        self.scopes = scope.split()
        self.client_id = client_id
        self.client_secret = client_secret