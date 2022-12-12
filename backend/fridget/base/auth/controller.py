from fridget.base.schema import User
from fastapi import Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from fridget.base.auth.auth import (
    authenticate_user,
    create_access_token,
    get_password_hash
)
from fridget.base.auth.models import OAuth2EmailPasswordRequestForm
from asyncpg.exceptions import UniqueViolationError


# This file controls authentication
class AuthController:
    def __init__(self):
        # we need this to send useful error messages to the FE
        self.error_dict = {
            "users_email_key": "Email",
            "users_username_key": "Username"
        }

    async def login_for_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()):
        user = await authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return create_access_token(user)

    # signs a user up
    async def sign_up(self, form_data: OAuth2EmailPasswordRequestForm = Depends()):
        hashed_password = get_password_hash(form_data.password)
        try:
            user = await User.objects.create(
                email=form_data.email,
                username=form_data.username,
                hashed_password=hashed_password,

            )
        except UniqueViolationError as e:
            # send a nice little error to the FE so we can simply add it as an error message for the end user
            error = self.error_dict[e.__dict__["constraint_name"]]
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail=f"{error} already exists.",
            )
        return create_access_token(user)

    def set_jwt_cookie(self, response: Response, access_token: str | None = None):
        if access_token is None:
            response.set_cookie(key="access_token", value="")
        response.set_cookie(
            key="access_token", 
            value=f"Bearer {access_token}", 
            httponly=True, 
            samesite=None
        )
        
        