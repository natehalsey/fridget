from fastapi import APIRouter
from fridget.admin.controller import download_db

router = APIRouter(
    prefix = "/admin"
)

@router.get("/reinit-db")
async def reinit_db():
    await download_db()