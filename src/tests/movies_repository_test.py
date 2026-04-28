import unittest
from entities.movies import Movies
from entities.user import User
from repositories.movies_repository import movies_repository
from repositories.user_repository import user_repository

class TestMoviesRepository(unittest.TestCase):
    def setUp(self):
        movies_repository.delete_all()
        user_repository.delete_everyone()

        self.movie_1 = Movies("movie1", "2001")
        self.movie_2 = Movies("movie2", "2002")

        self.user_matti = User("matti", "123")
        self.user_teppo = User("teppo", "456")

    def test_create_movie(self):
        movies_repository.create(self.movie_1)
        movies = movies_repository.find_all()

        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].title, self.movie_1.title)
    
    def test_set_seen(self):
        added_movie = movies_repository.create(self.movie_1)
        movies = movies_repository.find_all()

        self.assertEqual(movies[0].seen, False)

        movies_repository.set_seen(added_movie.id)

        movies = movies_repository.find_all()

        self.assertEqual(movies[0].seen, True)
    
    def test_set_stars(self):
        new_movie = movies_repository.create(self.movie_1)
        self.assertEqual(new_movie.stars, 0)
        movies_repository.set_stars(new_movie.id, 3)
        movies = movies_repository.find_all()
        self.assertEqual(movies[0].stars, 3)