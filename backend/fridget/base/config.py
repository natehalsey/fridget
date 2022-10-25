class Settings:
    DATABASE = "sqlite:///db.sqlite"
    API_HOST = "themealdb.p.rapidapi.com"
    API_KEY =  "eb35fcf224msh909175e8c268c99p18336bjsn1e11ec2eeddf"
    HEADERS = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

settings = Settings()