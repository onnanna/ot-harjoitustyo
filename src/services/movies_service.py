# sovelluslogiikasta vastaava luokka

from entities.user import User
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
    def __init__(self, movies_repository=default_movies_repository,
                  user_repository=default_user_repository):
        self._user = None
        self._movies_repository = movies_repository
        self._user_repository = user_repository

    def login(self, username, password):

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user
        return user

    def logout(self):
        self._user = None

    def create_user(self, username, password, login=True):
        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            raise UsernameAlreadyExistsError(f"Username {username} already exists")
        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user

        return user

    def set_movie_seen(self, movie_id):
        self._movies_repository.set_seen(movie_id)

    def get_unseen_movies(self):
        if not self._user:
            return []

        movies = self._movies_repository.find_by_username(self._user.username)
        unseen_movies = filter(lambda movie: not movie.done, movies)

        return list(unseen_movies)

    def get_current_user(self):
        return self._user

#    def set_movie_seen(movie_id):

movies_service = MoviesService()
