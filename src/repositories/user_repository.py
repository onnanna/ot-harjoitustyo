from entities.user import User
from database_connection import get_database_connection

def get_user_row(row):
    return User(row["username"], row["password"]) if row else None

class UserRepository:
    """Käyttäjiin liittyvistä tieokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.
        """

        self._connection = connection

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen perusteella.

        Args:
            username: Käyttäjätunnus, jonka käyttäjä palautetaan.
        
        Returns:
            Palauttaa User-olion, jos käyttäjätunnuksen käyttäjä on tietokannassa.
            Muuten palauttaa None.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )
        self._connection.commit()
        row = cursor.fetchone()
        return get_user_row(row)

    def create(self, user):
        """Tallentaa käyttäjän tietokantaan.

        Args:
            user: Tallenettava kättäjä User-olion
        
        Returns:
            Tallennettu käyttäjä User-oliona.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()
        return user

    def find_everyone(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa listan User-olioita.
        """

        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()

        return [get_user_row(row) for row in rows]

    def delete_everyone(self):
        """Poistaa kaikki käyttäjät.
        """

        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()

user_repository = UserRepository(get_database_connection())
