# käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka
from entities.user import User
from database_connection import get_database_connection

def get_user_row(row):
    return User(row["username"], row["password"]) if row else None

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )
        self._connection.commit()
        row = cursor.fetchone()
        return get_user_row(row)

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()
        return user

    def find_everyone(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()

        return [get_user_row(row) for row in rows]

    def delete_everyone(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()

user_repository = UserRepository(get_database_connection())
