import unittest
from repositories import movies_repository
from ui.ui import UI
from entities.movies import Movies
from entities.user import User
from services.movies_service import (
    MoviesService,
    InvalidCredentialsError,
    UsernameAlreadyExistsError
)


class FakeMoviesRepository:
    def __init__(self, movies=None):
        self.movies = movies or []
    
    def create(self, movie):
        self.movies.append(movie)
        return movie
    
    def find_all(self):
        return self.movies
    
    def find_by_username(self, username):
        user_movies = filter(
            lambda movie: movie.user and movie.user.username == username,
            self.movies
        )
        return list(user_movies)
    
    def set_seen(self, movie_id, seen=True):
        for movie in self.movies:
            if movie.id == movie_id:
                movie.seen = seen
                break

    def set_stars(self, movie_id, stars):
        for movie in self.movies:
            if movie.id == movie_id:
                movie.stars = stars
                break


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []
    
    def find_by_username(self, username):
        matching_users = filter(
            lambda user: user.username == username,
            self.users
        )
        matching_users_list = list(matching_users)

        return matching_users_list[0] if len(matching_users_list) > 0 else None

    def create(self, user):
        self.users.append(user)
        return user

class TestMovieService(unittest.TestCase):
    def setUp(self):
        self.movies_service = MoviesService(
            FakeMoviesRepository(),
            FakeUserRepository())
    
        self.movie_1 = Movies("test 1", 2020)
        self.movie_2 = Movies("test 2", 1999)
        self.movie_3 = Movies("test 3", 2003, "Adventure", "yes notes")
        self.user_matti = User("matti", "123")

    def login_user(self, user):
        self.movies_service.create_user(user.username, user.password)

    def test_create_movie(self):
        self.login_user(self.user_matti)

        self.movies_service.create_movie("testing movie", 1500)
        movies = self.movies_service.get_unseen_movies()

        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].title, "testing movie")
        self.assertEqual(movies[0].year, 1500)
        self.assertEqual(movies[0].user.username, self.user_matti.username)
    
    def test_create_movie_with_genre_and_notes(self):
        self.login_user(self.user_matti)

        self.movies_service.create_movie("testing genres", 2003, "Adventure", "yes to notes")
        movies = self.movies_service.get_unseen_movies()

        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].title, "testing genres")
        self.assertEqual(movies[0].year, 2003)
        self.assertEqual(movies[0].genre, "Adventure")
        self.assertEqual(movies[0].notes, "yes to notes")
        self.assertEqual(movies[0].user.username, self.user_matti.username)

    def test_unseen_movies(self):
        self.login_user(self.user_matti)
        self.movies_service.create_movie(self.movie_1.title, self.movie_1.year)
        created_movie_2 = self.movies_service.create_movie(self.movie_2.title, self.movie_2.year)
        self.movies_service.set_movie_seen(created_movie_2.id)
        unseen_moves = self.movies_service.get_seen_movies()

        self.assertEqual(len(unseen_moves), 1)
        self.assertEqual(unseen_moves[0].title, self.movie_2.title)

    def test_get_current_user(self):
        self.login_user(self.user_matti)
        current_user = self.movies_service.get_current_user()
        self.assertEqual(current_user.username, self.user_matti.username)

    def test_create_user_with_existing_username(self):
        username = self.user_matti.username
        self.movies_service.create_user(username, "salasana")

        self.assertRaises(
            UsernameAlreadyExistsError,
            lambda: self.movies_service.create_user(username, "jokumuusalasana")
        )

    def test_login_with_valid_username_and_password(self):
        self.movies_service.create_user(
            self.user_matti.username,
            self.user_matti.password
        )

        user = self.movies_service.login(
            self.user_matti.username,
            self.user_matti.password
        )
        self.assertEqual(user.username, self.user_matti.username)

    def test_login_with_invalid_username_and_password(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.movies_service.login("testaus", "väärä")
        )
    
    def test_create_user_without_login(self):
        username = "matti"
        password = "matti123"
        self.movies_service.create_user(username, password, login=False)
        user = self.movies_service.get_current_user()

        self.assertIsNone(user)
    
    def test_logout(self):
        self.movies_service.create_user(self.user_matti.username, self.user_matti.password)
        self.movies_service.login(self.user_matti.username, self.user_matti.password)
        self.movies_service.logout()
        
        self.assertIsNone(self.movies_service.get_current_user())

    def test_get_unseen_movies_without_user(self):
        movies = self.movies_service.get_unseen_movies()

        self.assertEqual(movies, [])

    def test_set_stars_for_movie_with_valid_stars(self):
        self.login_user(self.user_matti)
        movie = self.movies_service.create_movie(self.movie_1)

        self.assertEqual(movie.stars, 0)
        self.assertFalse(movie.seen)

        self.movies_service.set_stars_for_movie(movie.id, "3")

        self.assertEqual(movie.stars, 3)
        self.assertTrue(movie.seen)

    def test_set_stars_for_movie_with_invalid_stars(self):
        self.login_user(self.user_matti)
        movie = self.movies_service.create_movie(self.movie_1)

        self.movies_service.set_stars_for_movie(movie.id, "10")

        self.assertEqual(movie.stars, 0)


    def test_get_seen_movies_empty_list(self):
        self.movies_service.create_movie(self.movie_2)
        seen_movies = self.movies_service.get_seen_movies()
        self.assertEqual(seen_movies, [])
