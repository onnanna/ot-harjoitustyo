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
    
    def test_set_seen_with_nonexisting_id(self):
        movies_repository.create(self.movie_2)
        movies_repository.set_seen("id")

        self.assertFalse(self.movie_2.seen)

    
    def test_set_stars(self):
        new_movie = movies_repository.create(self.movie_1)

        self.assertEqual(new_movie.stars, 0)

        movies_repository.set_stars(new_movie.id, 3)
        movies = movies_repository.find_all()

        self.assertEqual(movies[0].stars, 3)
    
    def test_set_stars_with_non_existing_id(self):
        movies_repository.create(self.movie_1)
        movies_repository.set_stars("id", 5)

        self.assertEqual(self.movie_1.stars, 0)

    def test_find_by_username(self):
        matti = user_repository.create(self.user_matti)
        movie = Movies("movie1", "2001", user=matti)
        movies_repository.create(movie)

        movies = movies_repository.find_by_username(matti.username)

        self.assertEqual(movies[0].title, movie.title)
