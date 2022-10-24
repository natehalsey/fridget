
from fastapi import FastAPI

from .recipes.views import router as RecipeRouter


app = FastAPI()

app.include_router(RecipeRouter)