import unittest
from entities.user import User
from repositories.user_repository import user_repository

class TestMoviesRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_everyone()
        self.user_maija = User("maij", "maija123")

    def test_create_user(self):
        user_repository.create(self.user_maija)
        users = user_repository.find_everyone()
        self.assertEqual(len(users), 1)