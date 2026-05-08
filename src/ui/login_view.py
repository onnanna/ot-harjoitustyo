from tkinter import ttk, StringVar, constants
from services.movies_service import InvalidCredentialsError

class LoginView:
    """Käyttäjään kirjautumisesta vastaava näkymä."""
    def __init__(self, root, handle_login, handle_show_create_user_view=None):
        """Luokan konstruktori. Luo uuden näkymän kirjautumiselle.

        Args:
            root:
                Tkinter-elementti, jonka sisään alustetaan näkymä
            hande_login:
                Kutsuttava-arvo, jota kutsutaan käyttäjän kirjautuessa sisään
            handle_show_create_user_view:
                Kutstuttava-arvo, jota kutsutaan siirryttäessä rekisteröitymisnäkymään
        """
        self._root = root
        self._handle_login = handle_login
        self._handle_show_create_user_view = handle_show_create_user_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_label = None
        self.error_variable = None

        self._initialize()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login_handler
        )

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create user",
            command=self._handle_show_create_user_view or (lambda: None)
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
    
    def pack(self):
        """Näyttää näkymän"""
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        """Tuhoaa näkymän"""
        self._frame.destroy()
    
    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            self._handle_login(username, password)
        except InvalidCredentialsError:
            self._show_error("Invalid username or password")
    
    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):   
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    
    def _hide_error(self):
        self._error_label.grid_remove()