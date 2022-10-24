import ormar
from fastapi import APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from ..recipes.requests import RequestRecipes
from ..base.schema import Recipes
from typing import List



router = APIRouter(
    prefix = "/login"
)


@router.get("/")
async def login(username: str):
   pass 