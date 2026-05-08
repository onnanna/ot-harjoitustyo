from entities.user import User
from entities.movies import Movies
from repositories.movies_repository import (
    movies_repository as default_movies_repository
)
from repositories.user_repository import (
    user_repository as default_user_repository
)

class InvalidCredentialsError(Exception):
    pass

class UsernameAlreadyExistsError(Exception):
    pass


class MoviesService:
    """Sovelluslogiikasta vastaaa luokka."""
    def __init__(self, movies_repository=default_movies_repository,
                  user_repository=default_user_repository
    ):
        """Luokan konstruktori, joka luo uuden sovelluslogiikasta vastaavan palvelun.
        
        Args:
            movies_repository:
                Vapaaehtoinen, oletusarvoltaan MovieRepository-olio.
                Olio, jolla on MovieRepository-luokkaa vastaavat metodit.
            user_repository:
                Vapaaehtoinen, oleturarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """
        self._user = None
        self._movies_repository = movies_repository
        self._user_repository = user_repository

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Merkkijonoarvo, joka kuvaa sisäänkirjautuvan käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa sisäänkirjautuvan käyttäjän salasanaa.
        
        Returns:
            Kirjautunut käyttäjä User-oliona.
        
        Raises:
            InvalidCredentialsError:
                Virhe, joka tapahtuu, jos käyttäjätunnus ja salasana eivät täsmää.
        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user
        return user

    def logout(self):
        """Kirjaa nykyisen käyttäjän ulos.
        """
        self._user = None

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvastaa käyttäjän salasanaa.
            login:
                Vapaaehtoinen, oletusarvoltaan True
                Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen.
        
        Raises:
            UsernameAlreadyExistsError: Virhe, joka tapathuu, jos käyttäjätunnus on jo käytössä.
        
        Returns:
            Luotu käyttäjä User-olion muodossa.
        """

        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            raise UsernameAlreadyExistsError(f"Username {username} already exists")
        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user

        return user

    def set_stars_for_movie(self, movie_id, stars):
        """Asettaa elokuvan arvostelun.
        
        Args:
            movie_id: Merkkiarvojono, joka kuvaa elokuvan id:tä.
            stars: Merkkiarvojono, joka kuvaaa elokuvalle annettavaa arvostelua
        """

        stars = int(stars)
        if 1 <= stars <= 5:
            self._movies_repository.set_stars(movie_id, stars)
            self._movies_repository.set_seen(movie_id, True)

    def set_movie_seen(self, movie_id):
        """Asettaa elokuvan nähdyksi
        Args:
            movie_id: Merkkiarvojono, joka kuvaa elokuvan id:tä.
        """
        self._movies_repository.set_seen(movie_id, True)

    def get_unseen_movies(self):
        """Palauttaa käyttäjän näkemättömät elokuvat.

        Returns:
            Palauttaa kirjautuneen käyttäjän näkemättömät elokuvat Movie-olioiden listana.
            Jos ei ole kirjautunutta käyttäjää, palauttaa tyhjän listan.
        """
        if not self._user:
            return []

        movies = self._movies_repository.find_by_username(self._user.username)
        unseen_movies = filter(lambda movie: not movie.seen, movies)

        return list(unseen_movies)

    def get_seen_movies(self):
        """Palauttaa käyttäjän näkemät elokuvat.

        Returns:
            Palauttaa kirjautuneen käyttäjän näkemät elokuvat Movie-olioiden listana.
            Jos ei ole kirjautunutta käyttäjää, palauttaa tyhjän listan.
        """
        if not self._user:
            return []

        movies = self._movies_repository.find_by_username(self._user.username)
        seen_movies = filter(lambda movie: movie.seen, movies)

        return list(seen_movies)

    def get_current_user(self):
        """Palauttaa kirjautuneen käyttäjän
        
        Returns:
            Kirjautunut käyttäjä User-oliona
        """

        return self._user

    def create_movie(self, title, year=None, genre=None, notes=None):
        """Luo uuden elokuvan
        
        Args:
            title: Merkkijonoarvo, joka kuvaa elokuvan nimeä
            year:
                Vapaaehtoinen, oletusarvoltaan None
                Merkkijonoarvo, joka kuvaa elokuvan julkaisuvuotta
            genre:
                Vapaaehtoinen, oletusarvoltaan None
                Merkkijonoarvo, joka kuvaa elokuvan genreä
            notes:
                Vapaaehtoinen, oletusarvoltaan None
                Merkkijonoarvo, joka kuvaa elokuvan lisätietoja
                
        Returns:
            Luotu elokuva Movie-oliona.
        """
        movie = Movies(
            title=title,
            year=year,
            genre=genre,
            notes=notes,
            user=self._user
        )
        return self._movies_repository.create(movie)

movies_service = MoviesService()
