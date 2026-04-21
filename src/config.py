import os
import importlib
from pathlib import Path

#tekoälyn koodi alkaa
def load_dotenv(*args, **kwargs):
    try:
        dotenv_module = importlib.import_module("dotenv")
    except ImportError:
        return False

    return dotenv_module.load_dotenv(*args, **kwargs)

dirname = os.path.dirname(__file__)
base_dir = Path(__file__).resolve().parent

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

MOVIES_FILE_NAME = os.getenv("MOVIES_FILE_NAME") or "movies.csv"
MOVIES_FILE_PATH = str(base_dir.parent / "data" / MOVIES_FILE_NAME)

DATABASE_FILE_NAME = os.getenv("DATABASE_FILE_NAME") or "database.sqlite"
DATABASE_FILE_PATH = str(base_dir.parent / "data" / DATABASE_FILE_NAME)
#tekoälyn koodi loppuu
