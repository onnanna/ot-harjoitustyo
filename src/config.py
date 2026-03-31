import os
import importlib

#tekoälyn koodi alkaa
def load_dotenv(*args, **kwargs):
    try:
        dotenv_module = importlib.import_module("dotenv")
    except ImportError:
        return False

    return dotenv_module.load_dotenv(*args, **kwargs)
#tekoälyn koodi loppuu

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

MOVIES_FILE_NAME = os.getenv("MOVIES_FILE_NAME") or "movies.csv"
MOVIES_FILE_PATH = os.path.join(dirname, "..", "data", MOVIES_FILE_NAME)

DATABASE_FILE_NAME = os.getenv("DATABASE_FILE_NAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILE_NAME)
