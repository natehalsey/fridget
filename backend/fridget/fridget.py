
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .wrapper.views import router as WrapperRouter
from .base.login import router as LoginRouter


app = FastAPI()


origins = [
    "https://localhost:3000",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(LoginRouter)
app.include_router(WrapperRouter)
