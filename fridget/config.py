from dotenv import load_dotenv

load_dotenv()

# to be made into env variables
class Settings:
    DATABASE = "sqlite:///db.sqlite"
    
    RECIPE_API_URL = "themealdb.p.rapidapi.com"
    RECIPE_API_KEY =     "eb35fcf224msh909175e8c268c99p18336bjsn1e11ec2eeddf", #secret
    RECIPE_HEADERS = {
        "X-RapidAPI-Key" : RECIPE_API_KEY,
        "X-RapidAPI-Host" : RECIPE_API_URL
    }
    
    # randomly generated
    APP_SECRET_KEY="3100ec29910a9715ad2182e23a3d2d08e724d249d09ba89efbe035cbb5db9d14"

settings = Settings()  