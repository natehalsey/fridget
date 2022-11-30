import os

################################
#os.environ["DATABASE_URL"] = "postgresql://dev:fridget@172.17.0.2:5432/postgres" #postgresql://postgres:SRql605syVtnpUtP@74.119.150.172:5432/fridget"
#os.environ["SECRET_KEY"] = "8707c3c1c1938e0934c67a8e54dddadd6be0621aaba8dcc8cc90d7aaecd9ab3c"
################################

class Settings:
    DATABASE_URL = os.environ.get("DATABASE_URL")# env var
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 300

settings = Settings()