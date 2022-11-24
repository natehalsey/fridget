
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fridget.base.schema import database
from fridget.users.views import router as UserRouter
from fridget.recipes.views import router as RecipeRouter
from fridget.ingredients.views import router as IngredientRouter

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
app.include_router(IngredientRouter)
app.include_router(RecipeRouter)
app.include_router(UserRouter)

@app.on_event("startup")
async def startup() -> None:
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    if database.is_connected:
        await database.disconnect()