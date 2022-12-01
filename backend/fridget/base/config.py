# some config or env variables, should be secrets
class Settings:
    DATABASE_URL = "postgresql://postgres:SRql605syVtnpUtP@74.119.150.172:5432/fridget" # env var
    SECRET_KEY = "8707c3c1c1938e0934c67a8e54dddadd6be0621aaba8dcc8cc90d7aaecd9ab3c" # change to env var
    ALGORITHM = "HS256" 
    ACCESS_TOKEN_EXPIRE_MINUTES = 300

settings = Settings()