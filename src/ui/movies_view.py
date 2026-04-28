from tkinter import ttk, constants
from services.movies_service import movies_service

class MoviesListView:
    def __init__(self, root, movies, handle_movie_set_stars, show_dropdown=True):
        self._root = root
        self._movies = movies
        self._handle_movie_set_stars = handle_movie_set_stars
        self._show_dropdown = show_dropdown
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_movie_item(self, movie):
        item_frame = ttk.Frame(master=self._frame)

        label_text = f"{movie.title} ({movie.year})" if movie.year else movie.title
        label = ttk.Label(master=item_frame, text=label_text)
        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        if self._show_dropdown:
            dropdown = ttk.Combobox(
                master=item_frame,
                values=["1", "2", "3", "4", "5"],
                state="readonly",
                width=4
            )
            dropdown.grid(row=0, column=1, padx=5, pady=5, sticky=constants.E)
            dropdown.bind(
                "<<ComboboxSelected>>",
                lambda _event, movie_id=movie.id, combobox=dropdown: self._handle_movie_set_stars(movie_id, combobox.get())
            )
        else:
            stars_label = ttk.Label(master=item_frame, text=movie.stars * "★")
            stars_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.E)

        details_frame = ttk.Frame(master=item_frame)
        genre_text = movie.genre if movie.genre else "-"
        notes_text = movie.notes if movie.notes else "-"

        genre_label = ttk.Label(master=details_frame, text=f"Genre: {genre_text}")
        genre_label.grid(row=0, column=0, padx=5, pady=(0, 2), sticky=constants.W)

        notes_label = ttk.Label(master=details_frame, text=f"Notes: {notes_text}")
        notes_label.grid(row=1, column=0, padx=5, pady=(0, 5), sticky=constants.W)

        show_more_button = ttk.Button(master=item_frame, text="Show more", width=10)

        def info_details():
            if details_frame.winfo_ismapped():
                details_frame.grid_remove()
                show_more_button.configure(text="Show more")
            else:
                details_frame.grid(row=1, column=0, columnspan=3, sticky=constants.W)
                show_more_button.configure(text="Hide")

        show_more_button.configure(command=info_details)
        show_more_button.grid(row=0, column=2, padx=5, pady=5, sticky=constants.E)
        details_frame.grid_remove()
        
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
        self._create_movie_title_entry = None
        self._create_movie_year_entry = None
        self._title_label = None
        self._year_label = None
        self._movie_list_frame = None
        self._movie_list_view = None
        self._seen_movie_frame = None
        self._seen_movie_view = None
        self._create_movie_genre = None
        self._create_movie_notes = None
        self._more_frame = None
        self._more_expanded = False

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        movies_service.logout()
        self._handle_logout()
       
    def _handle_set_movie_stars(self, movie_id, stars):
        movies_service.set_stars_for_movie(movie_id, stars)
        self._initialize_movie_list()
        self._initialize_seen_movie_list()

    def handle_more_info(self):
        if self._more_expanded:
            self._more_frame.grid_remove()
            self._more_expanded = False
            return
        self._more_frame.grid(
            row=3,
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            sticky=constants.EW
        )
        self._more_expanded = True

    def _initialize_movie_list(self):
        if self._movie_list_view:
            self._movie_list_view.destroy()

        movies = movies_service.get_unseen_movies()

        self._movie_list_view = MoviesListView(
            self._movie_list_frame,
            movies,
            self._handle_set_movie_stars
        )
        self._movie_list_view.pack()     

    def _initialize_seen_movie_list(self):
        if self._seen_movie_view:
            self._seen_movie_view.destroy()

        movies = movies_service.get_seen_movies()

        self._seen_movie_view = MoviesListView(
            self._seen_movie_frame,
            movies, 
            self._handle_set_movie_stars,
            show_dropdown=False
        )
        self._seen_movie_view.pack() 

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

    def _handle_create_movie(self):
        movie_title = self._create_movie_title_entry.get().strip()
        movie_year = self._create_movie_year_entry.get().strip()
        genre = self._create_movie_genre.get() if self._create_movie_genre else None
        notes = self._create_movie_notes.get() if self._create_movie_notes else None

        if not movie_title:
            return

        movies_service.create_movie(movie_title, movie_year or None, genre or None, notes or None)
        self._initialize_movie_list()
        self._create_movie_title_entry.delete(0, constants.END)
        self._create_movie_year_entry.delete(0, constants.END)
        self._create_movie_genre.set("")
        self._create_movie_notes.delete(0, constants.END)

    def _initialize_footer(self):
        self._create_movie_title_entry = ttk.Entry(master=self._frame)
        self._create_movie_year_entry = ttk.Entry(master=self._frame)
        button_frame = ttk.Frame(master=self._frame)

        create_movie_button = ttk.Button(
            master=button_frame,
            text="Add new movie",
            command=self._handle_create_movie
        )
        more_button = ttk.Button(
            master=button_frame,
            text="More",
            command=self.handle_more_info
        )
        self._create_movie_title_entry.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )
        self._create_movie_year_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )
        create_movie_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)
        more_button.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )
        button_frame.grid(
            row=2,
            column=2,
            sticky=constants.EW
        )

        self._more_frame = ttk.Frame(master=self._frame)

        genre_label = ttk.Label(master=self._more_frame, text="Genre:")
        genre_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        self._create_movie_genre = ttk.Combobox(
            master=self._more_frame,
            values=["Action", "Adventure","Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Fantacy", "Historical", "Other"],
            state="readonly"
        )
        self._create_movie_genre.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)
        
        notes_label = ttk.Label(master=self._more_frame, text="Notes:")
        notes_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        
        self._create_movie_notes = ttk.Entry(master=self._more_frame, width=30)
        self._create_movie_notes.grid(
            row=1, 
            column=1, 
            padx=5, 
            pady=5, 
            sticky=constants.EW)
        self._more_frame.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._movie_list_frame = ttk.Frame(master=self._frame)
        self._seen_movie_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_movie_list()
        self._initialize_seen_movie_list()
        self._initialize_footer()

        self._movie_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._seen_movie_frame.grid(
            row=4,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)