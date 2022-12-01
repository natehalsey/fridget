# this file contains all of the necessary functions to make authentication possible
import ormar
from jose import JWTError, jwt
from fridget.base.schema import User
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fridget.base.config import Settings
from fridget.base.auth.models import TokenData
from fastapi.security import OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi import Request
from fastapi.security.utils import get_authorization_scheme_param
from fastapi import HTTPException
from fastapi import status
from typing import Optional
from typing import Dict

# define a new custom class that fetches the auth token from cookies


class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(
            password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        # this line gets the access token from the cookies
        authorization: str = request.cookies.get("access_token")

        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param


oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/auth/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    It takes a plain text password and a hashed password and returns True if the plain text password
    matches the hashed password

    :param plain_password: The password that the user entered
    :type plain_password: str
    :param hashed_password: The hashed password that you want to verify
    :type hashed_password: str
    :return: A boolean value.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    It takes a password and returns a hashed password

    :param password: The password to hash
    :type password: str
    :return: A string
    """
    return pwd_context.hash(password)


async def get_user(username: str) -> User | None:
    """
    "Gets a user object by username, or return None if no user is found."

    :param username: str - This is the username of the user we want to get
    :type username: str
    :return: User object or None
    """
    try:
        user: User = await User.objects.get(
            username=username
        )
    except ormar.NoMatch:
        return None

    return user


async def authenticate_user(username: str, password: str):
    """
    "If the user exists and the password is correct, return the user, otherwise return False."

    The first thing we do is get the user from the database. If the user doesn't exist, we return False.
    If the user does exist, we verify the password. If the password is incorrect, we return False. If
    the password is correct, we return the user

    :param username: str - The username of the user to authenticate
    :type username: str
    :param password: The password that the user entered
    :type password: str
    :return: A user object
    """

    user: User = await get_user(username)
    if not user or not verify_password(password, user.hashed_password):
        return False

    return user


def create_access_token(user: User):
    """
    It creates a JWT token with a subject of the user's username, and an expiration time of 15 minutes

    :param user: User: This is the user object that we want to create the access token for
    :type user: User
    :return: A dictionary with the access token and the token type.
    """
    access_token_expires = timedelta(
        minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = _create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def _create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Creates the JWT token for the given data


    :param data: The data to be encoded
    :type data: dict
    :param expires_delta: This is the time in which the token will expire
    :type expires_delta: timedelta | None
    :return: A string
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, Settings.SECRET_KEY, algorithm=Settings.ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    It takes a token, decodes it, and returns the user associated with the token

    :param token: str = Depends(oauth2_scheme)
    :type token: str
    :return: The user object
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, Settings.SECRET_KEY,
                             algorithms=[Settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """
    "Get the current user, and if there is no current user, return a 401 Unauthorized response."

    :param current_user: User = Depends(get_current_user)
    :type current_user: User
    :return: The current user
    """
    return current_user
