from requests import request, RequestException 
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from .schema import Users


router = APIRouter(
    prefix = "/login"
)
## User Endpoints - DB
@router.post('/new_user')
async def new_user(user: Users):
    print(user)
    # user.password = hash(user.password) can this be add at ORM/DB level?
    await user.save()
    return HTMLResponse(content="<h3>OK</h3>", status_code=200)

@router.post('/')
async def login(username: str, password: str ):
    return await Users.objects.get(username=username, hashed_password=password)