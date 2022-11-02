from fastapi import APIRouter
from .models import LoginRequestModel
from fridget.base.schema import User


router = APIRouter(
    prefix = "/login"
)

@router.post('')
async def login(user_info: LoginRequestModel):
    user, _ = await User.objects.get_or_create(
        given_name= user_info.given_name,
        family_name= user_info.family_name,
        picture= user_info.picture,
        email= user_info.email
    )

    return user.id