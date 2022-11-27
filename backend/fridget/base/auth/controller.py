from fridget.base.schema import User
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from fridget.base.auth.auth import (
    authenticate_user, 
    create_access_token,
    get_password_hash
)
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
    
    async def sign_up(self, form_data: OAuth2PasswordRequestForm = Depends()):
        hashed_password = get_password_hash(form_data.password)
        try:
            user = await User.objects.create(
                username=form_data.username,
                hashed_password=hashed_password,
            )
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Username already exists"
            )

        return create_access_token(user)