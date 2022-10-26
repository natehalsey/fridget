

from requests import request, RequestException 
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from .schema import Users
from contoller import CategoryContoller

router = APIRouter(
    prefix = "/categories"
)
## User Endpoints - DB
@router.get('/search')
async def search(q: str):
    await CategoryContoller.test()

@router.get('/get_all')
async def getall():
    pass

