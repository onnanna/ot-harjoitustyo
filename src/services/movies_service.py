# sovelluslogiikasta vastaava luokka

#from entities.movies import Movies
from entities.user import User


class InvalidCredentialsError(Exception):
    pass

class UsernameAlreadyExistsError(Exception):
    pass

class MoviesService:
    def __init__(self, movies_repository, user_repository):
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

    def _create_user(self, username, password, login = True):

        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            raise UsernameAlreadyExistsError(f"Username {username} already exists")
        
        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user
        
        return user