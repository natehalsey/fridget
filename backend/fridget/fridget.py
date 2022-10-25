
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .wrapper.views import router as WrapperRouter
from .base.login import router as LoginRouter


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(LoginRouter)
app.include_router(WrapperRouter)
