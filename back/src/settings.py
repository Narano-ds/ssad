import os

class Settings:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevSettings(Settings):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", None)


class ProdSettings(Settings):
    DEBUG = False
