# elokuviin liittyvistä tietokantaoperaatioista vastaava luokka

#from entities.movies import Movie
#from repositories.user_repository import UserRepository
#from config import TO

class MoviesRepository:
    def __init__(self, file_path):
        self._file_path = file_path        