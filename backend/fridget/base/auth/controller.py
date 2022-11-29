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

error_dict = {
    "users_email_key": "Email",
    "users_username_key": "Username"
}

class AuthController:    
    async def login_for_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()):
        user = await authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return create_access_token(user)
    
    async def sign_up(self, form_data: OAuth2EmailPasswordRequestForm = Depends()):
        hashed_password = get_password_hash(form_data.password)
        try: 
            user = await User.objects.create(
                email=form_data.email,
                username=form_data.username,
                hashed_password=hashed_password,
                
            )
        except UniqueViolationError as e:
            error = error_dict[e.__dict__["constraint_name"]]
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{error} already exists.")

        return create_access_token(user)