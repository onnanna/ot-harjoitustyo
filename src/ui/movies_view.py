from tkinter import ttk, constants
from services.movies_service import movies_service

class MoviesListView:
    def __init__(self, root, movies, handle_movie_watched):
        self._root = root
        self._movies = movies
        self._handle_movie_watched = handle_movie_watched
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_movie_item(self, movie):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=movie.content)

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        set_star_button = ttk.Button(
        master=item_frame,
        text="★",
        font=("Arial", 20),
        fg="gold",
        bg="white",
        bd=0,
        activeforeground="gold",
        activebackground="white",
        command=lambda: self._handle_movie_watched(movie.id)
        )
        set_star_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.E
        )
        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for movie in self._movies:
            self._initialize_movie_item(movie)

class MoviesView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = movies_service.get_current_user()
        self._frame = None
        self._create_movie_entry = None
        self._movie_list_frame = None
        self._movie_list_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        movies_service.logout()
        self._handle_logout()

    def _handle_set_movie_seen(self, movie_id):
        movies_service.set_movie_seen(movie_id)
        self._initialize_movie_list()

    def _initialize_movie_list(self):
        if self._movie_list_view:
            self._movie_list_view.destroy()

        movies = movies_service.get_unseen_movies()

        self._movie_list_view = MoviesListView(
            self._movie_list_frame,
            movies,
            self._handle_set_movie_seen
        )
        self._movie_list_view.pack()


    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Logged in as {self._user.username}"
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._logout_handler
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

#    def _handle_create_movie(self):
 
    def _initialize_footer(self):
        self._create_movie_entry = ttk.Entry(master=self._frame)

        create_movie_button = ttk.Button(
            master=self._frame,
            text="Add",
            #command=self._handle_create_movie
        )

        create_movie_button.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._movie_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_movie_list()
        self._initialize_footer()

        self._movie_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)