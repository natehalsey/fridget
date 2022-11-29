# Imports ############################
# Base
from fastapi import FastAPI

# Routers
from fridget.users.views import router as UserRouter
from fridget.recipes.views import router as RecipeRouter
from fridget.base.auth.views import router as AuthRouter

# Middleware
import time
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

# DB
from fridget.base.schema import database


# Base ###############################
app = FastAPI()



# Routers ############################
app.include_router(RecipeRouter)
app.include_router(UserRouter)
app.include_router(AuthRouter)


# Middleware ########################
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://fridget.co"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# DB ##################################
@app.on_event("startup")
async def startup() -> None:
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    if database.is_connected:
        await database.disconnect()
        