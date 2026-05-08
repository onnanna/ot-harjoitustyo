import unittest
from entities.user import User
from repositories.user_repository import user_repository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_everyone()
        self.user_matti = User("matti", "123")
        self.user_teppo = User("teppo", "456")

    def test_create_user(self):
        user_repository.create(self.user_matti)
        users = user_repository.find_everyone()

        self.assertEqual(len(users), 1)

        self.assertEqual(users[0].username, self.user_matti.username)

    def test_find_everyone(self):
        user_repository.create(self.user_matti)
        user_repository.create(self.user_teppo)
        users = user_repository.find_everyone()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_matti.username)
        self.assertEqual(users[1].username, self.user_teppo.username)
    
    def test_find_by_username(self):
        user_repository.create(self.user_matti)
        user = user_repository.find_by_username(self.user_matti.username)

        self.assertEqual(user.username, self.user_matti.username)
