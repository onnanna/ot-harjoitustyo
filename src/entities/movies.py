# luokka joka kuvaa yksittäistä elokuvaa
import uuid

class Movies:

    def __init__(self, name, seen=False, user=None, movie_id=None, stars=0):
        self.name = name
        self.seen = seen
        self.user = user
        self.id = movie_id if movie_id else str(uuid.uuid4())
        self.stars = stars
