# the config setting for the backend
from pydantic import BaseSettings
class Settings(BaseSettings):
    DATABASE_URL = 'postgresql://postgres@localhost:5432/fridget'
    AUTH_TOKEN_API_KEY = 'fridget-be-key'

settings = Settings()