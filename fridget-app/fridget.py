
from fastapi import FastAPI
from .ingredients.views import router as IngredientRouter

app = FastAPI()

app.include_router(IngredientRouter)