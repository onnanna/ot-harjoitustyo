# luokka joka kuvaa yksittäistä elokuvaa
import uuid

class Movies:

    def __init__(self, name, watched=False, user=None, movie_id=None, stars=0):
        self.name = name
        self.watched = watched
        self.user = user
        self.id = movie_id if movie_id else str(uuid.uuid4())
        self.stars = stars
