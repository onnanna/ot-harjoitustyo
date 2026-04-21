import sqlite3
from pathlib import Path
from config import DATABASE_FILE_PATH

Path(DATABASE_FILE_PATH).parent.mkdir(parents=True, exist_ok=True)
connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
