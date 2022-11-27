from fastapi import APIRouter, Depends
from fridget.base.auth.models import Token
from fastapi.security import OAuth2PasswordRequestForm
from fridget.base.auth.controller import AuthController

router = APIRouter(
    prefix="/auth"
)

auth_controller = AuthController()

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return await auth_controller.login_for_access_token(form_data)

@router.post("/sign-up", response_model=Token)
async def sign_up(form_data: OAuth2PasswordRequestForm = Depends()):
    return await auth_controller.sign_up(form_data)