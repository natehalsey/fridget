
from fastapi import FastAPI
from .ingredients.views import router as IngredientRouter
from .recipes.views import router as RecipeRouter


app = FastAPI()

app.include_router(IngredientRouter)
app.include_router(RecipeRouter)