
from fastapi import APIRouter, Depends, Response
from fridget.base.auth.models import Token
from fastapi.security import OAuth2PasswordRequestForm
from fridget.base.auth.models import OAuth2EmailPasswordRequestForm
from fridget.base.auth.controller import AuthController

router = APIRouter(
    prefix="/auth"
)

auth_controller = AuthController()

@router.post("/login")
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    token = await auth_controller.login_for_access_token(form_data)
    auth_controller.set_jwt_cookie(response, token["access_token"])


@router.post("/sign-up")
async def sign_up(response: Response, form_data: OAuth2EmailPasswordRequestForm = Depends()):
    token = await auth_controller.sign_up(form_data)
    auth_controller.set_jwt_cookie(response,  token["access_token"])


@router.post("/logout")
async def logout(response: Response):
    auth_controller.set_jwt_cookie(response)
