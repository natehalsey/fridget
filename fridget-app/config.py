from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# to be made into env variables
class Settings:
    DATABASE = "sqlite:///db.sqlite"
    RECIPE_API_URL = "https://api.spoonacular.com/recipes/complexSearch"
    RECIPE_API_KEY =  "" # keep it secret, keep it safe
    RECIPE_HEADERS = {
       "" : API_KEY
    }

settings = Settings()