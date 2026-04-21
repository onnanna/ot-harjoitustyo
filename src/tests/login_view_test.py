import unittest
from ui.ui import UI
from ui.login_view import LoginView

class TestLoginView(unittest.TestCase):
    def setUp(self):
        self.ui = UI(None)

    def test_show_login_view(self):
        self.ui._show_login_view()
        self.assertIsNotNone(self.ui._current_view)
