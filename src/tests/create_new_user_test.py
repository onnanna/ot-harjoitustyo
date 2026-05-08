import unittest
from ui.ui import UI

class TestCreateNewUserView(unittest.TestCase):
    def setUp(self):
        self.ui = UI(None)

    def test_show_create_new_user_view(self):
        self.ui._show_create_user_view()
        self.assertIsNotNone(self.ui._current_view)
