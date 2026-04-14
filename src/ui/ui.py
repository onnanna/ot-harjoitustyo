from ui.login_view import LoginView
from ui.create_new_user import CreateUserView
from ui.movies_view import MoviesView
from services.movies_service import movies_service

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        self._show_login_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        
        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(self._root, self._handle_login, self.show_create_user_view)

        self._current_view.pack()

    def show_create_user_view(self):
        self._hide_current_view()
        self._current_view = CreateUserView(self._root, self._show_login_view)
        self._current_view.pack()

    def _show_movies_view(self):
        self._hide_current_view()
        self._current_view = MoviesView(self._root, self._handle_logout)
        self._current_view.pack()

    def _handle_login(self, username, password):
        movies_service.login(username, password)
        self._show_movies_view()

    def _handle_logout(self):
        movies_service.logout()
        self._show_login_view()