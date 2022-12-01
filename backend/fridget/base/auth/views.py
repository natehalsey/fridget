
from fastapi import APIRouter, Depends, Response
from fridget.base.auth.models import Token
from fastapi.security import OAuth2PasswordRequestForm
from fridget.base.auth.models import OAuth2EmailPasswordRequestForm
from fridget.base.auth.controller import AuthController

router = APIRouter(
    prefix="/auth"
)

auth_controller = AuthController()


# The views required for auth
@router.post("/login")
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    token = await auth_controller.login_for_access_token(form_data)
    access_token = token["access_token"]
    response.set_cookie(key="access_token",value=f"Bearer {access_token}", httponly=True, samesite=None)  #set HttpOnly cookie in response

@router.post("/sign-up")
async def sign_up(response: Response, form_data: OAuth2EmailPasswordRequestForm = Depends()):
    token = await auth_controller.sign_up(form_data)
    access_token = token["access_token"]
    response.set_cookie(key="access_token",value=f"Bearer {access_token}", httponly=True, samesite=None)  #set HttpOnly cookie in response

@router.post("/logout")
async def logout(response: Response):
    response.set_cookie(key="access_token", value="")