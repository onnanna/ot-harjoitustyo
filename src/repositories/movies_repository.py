from pathlib import Path
from entities.movies import Movies
from repositories.user_repository import user_repository
from config import MOVIES_FILE_PATH

class MoviesRepository:
    """Elokuviin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, file_path):
        """Luokan kostruktori.

        Args:
            file_path: Polku tiedostoon, johon tiedot elokuvista tallennetaan.
        """

        self._file_path = file_path

    def find_all(self):
        """Palauttaa kaikki elokuvat.

        Returns:
            Lista Movies-olioita.
        """

        return self._read()

    def _read(self):
        movies = []
        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                movie_id = parts[0]
                title = parts[1]
                year = parts[2]
                seen = parts[3] == "1"
                username = parts[4]
                stars = int(parts[5]) if len(parts) > 5 and parts[5].isdigit() else 0
                genre = parts[6] if len(parts) > 6 and parts[6] else None
                notes = parts[7] if len(parts) > 7 and parts[7] else None
                user = user_repository.find_by_username(
                    username) if username else None

                movies.append(
                    Movies(title, year, seen, user, movie_id, stars, genre, notes)
                )

        return movies

    def _write(self, movies):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for movie in movies:
                seen_string = "1" if movie.seen else "0"
                username = movie.user.username if movie.user else ""
                year = movie.year if movie.year else ""
                stars = str(movie.stars) if movie.stars else "0"
                genre = movie.genre if movie.genre else ""
                notes = movie.notes if movie.notes else ""

                row = (
                    f"{movie.id};{movie.title};{year};{seen_string};"
                    f"{username};{stars};{genre};{notes}"
                )

                file.write(row+"\n")

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def create(self, movie):
        """Tallentaa uuden elokuvan tietokantaan.

        Args:
            movie: Tallennettava elokuva Movies-oliona.

        Returns:
            Tallennettu elokuva Movies-oliona.
        """

        movies = self.find_all()
        movies.append(movie)
        self._write(movies)
        return movie

    def set_stars(self, movie_id, stars):
        """Asettaa elokuvan arvostelun.

        Args:
            movie_id: Elokuvan id, jonka arvostelu asetetaan.
            stars: Arvostelun tähtiarvion määrä.
        """

        movies = self.find_all()
        for movie in movies:
            if movie.id == movie_id:
                movie.stars = stars
                break

        self._write(movies)

    def set_seen(self, movie_id, seen=True):
        """Asettaa elokuvan nähdyksi.
        Args:
            movie_id: Elokuvan id, joka asetetaan nähdyksi.
            seen: 
                Vapaaehtoinen, oletusarvoltaan True
                Boolean-arvo, joka kuvaa asetetaanko elokuva nähdyksi vai ei
        """

        movies = self.find_all()
        for movie in movies:
            if movie.id == movie_id:
                movie.seen = seen
                break

        self._write(movies)

    def find_by_username(self, username):
        """Palauttaa käyttäjän elokuvat.
        Args:
            username: Käyttäjän käyttäjätunnus, jonka elokuvat palautetaan.
        Returns:
            Palauttaa listan Movies-olioita.
        """

        movies = self.find_all()
        user_movies = filter(
            lambda movie: movie.user and movie.user.username == username, movies)
        return list(user_movies)

    def delete_all(self):
        """Poistaa kaikki elokuvat.
        """

        self._write([])

movies_repository = MoviesRepository(MOVIES_FILE_PATH)
