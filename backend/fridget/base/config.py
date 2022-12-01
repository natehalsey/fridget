# the config setting for the backend
class Settings:
    DATABASE_URL = "postgresql://postgres:SRql605syVtnpUtP@74.119.150.172:5432/fridget"
    SECRET_KEY = "8707c3c1c1938e0934c67a8e54dddadd6be0621aaba8dcc8cc90d7aaecd9ab3c"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 300


settings = Settings()
