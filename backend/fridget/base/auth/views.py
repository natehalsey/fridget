
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
    """
    A function that takes in a response object and a form_data object. It then calls the
    login_for_access_token function in the auth_controller.py file. It then sets the access_token cookie
    in the response object.

    :param response: Response - this is the response object that will be returned to the client
    :type response: Response
    :param form_data: OAuth2PasswordRequestForm = Depends()
    :type form_data: OAuth2PasswordRequestForm
    """
    token = await auth_controller.login_for_access_token(form_data)
    access_token = token["access_token"]
    # set HttpOnly cookie in response
    response.set_cookie(
        key="access_token", value=f"Bearer {access_token}", httponly=True, samesite=None)


@router.post("/sign-up")
async def sign_up(response: Response, form_data: OAuth2EmailPasswordRequestForm = Depends()):
    """
    It signs up a user and sets a cookie in the response.

    :param response: Response - this is the response object that will be returned to the client
    :type response: Response
    :param form_data: OAuth2EmailPasswordRequestForm = Depends()
    :type form_data: OAuth2EmailPasswordRequestForm
    """
    token = await auth_controller.sign_up(form_data)
    access_token = token["access_token"]
    # set HttpOnly cookie in response
    response.set_cookie(
        key="access_token", value=f"Bearer {access_token}", httponly=True, samesite=None)


@router.post("/logout")
async def logout(response: Response):
    """
    It sets the value of the cookie named "access_token" to an empty string

    :param response: Response - The response object that will be returned to the client
    :type response: Response
    """
    response.set_cookie(key="access_token", value="")
