from fastapi import APIRouter, Depends, Response
from fridget.base.auth.models import Token
from fastapi.security import OAuth2PasswordRequestForm
from fridget.base.auth.controller import AuthController

router = APIRouter(
    prefix="/auth"
)

auth_controller = AuthController()

@router.post("/login", response_model=Token)
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    token = await auth_controller.login_for_access_token(form_data)
    access_token = token["access_token"]
    response.set_cookie(key="access_token",value=f"Bearer {access_token}", httponly=True, samesite=None)  #set HttpOnly cookie in response
    return token

@router.post("/sign-up", response_model=Token)
async def sign_up(form_data: OAuth2PasswordRequestForm = Depends()):
    return await auth_controller.sign_up(form_data)

@router.post("/logout")
async def logout(response: Response):
    response.set_cookie(key="access_token", value="")