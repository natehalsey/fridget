from fridget.base.schema import User
from fastapi import APIRouter, Depends
from fridget.base.auth.models import Token
from fridget.users.controller import UserController
from fastapi.security import OAuth2PasswordRequestForm
from fridget.users.models import UserModel
from fridget.base.auth.auth import get_current_active_user

router = APIRouter(
    prefix="/users"
)

user_controller = UserController()

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return await user_controller.login_for_access_token(form_data)

@router.post("/sign-up", response_model=Token)
async def sign_up(form_data: OAuth2PasswordRequestForm = Depends()):
    return await user_controller.sign_up(form_data)


@router.get("/get-user", response_model=UserModel)
async def get_user(current_user: User = Depends(get_current_active_user)):
    return current_user
    
    
# debugging only, remove before prod
@router.get("/get-users", response_model=list[UserModel])
async def get_users() -> list[User]:
    return await user_controller.get_users()

