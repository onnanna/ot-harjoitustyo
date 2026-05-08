from tkinter import ttk, StringVar, constants
from services.movies_service import movies_service, UsernameAlreadyExistsError

class CreateUserView:
    """Käyttäjän rekisteröitymisestä vastaava näkymä."""
    def __init__(self, root, handle_show_login_view):
        """Luokan konstruktori. Luo uuden näkymän rekisteröitymiselle.

        Args:
            root:
                Tkinter-elementti, jonka sisään alustetaan näkymä
            handle_show_login_view:
                Kutsuttava-arvo, jota kutsutaan, kun halutaan siirtyä takaisin login-näkymään
        """
        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_label = None
        self._error_variable = None

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

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create user",
            command=self._create_user_handler
        )

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_show_login_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        back_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
    
    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()
    
    def _hide_error(self):
        self._error_label.grid_remove()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Username and password is required")
            return

        if len(username) < 3:
            self._show_error("Username must be at least 3 characters long")
            return

        if len(password) < 5:
            self._show_error("Password must be at least 5 characters long")
            return

        try:
            movies_service.create_user(username, password)
            self._handle_show_login_view()
        except UsernameAlreadyExistsError:
            self._show_error(f"Username {username} already exists")
            self._handle_show_login_view()

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