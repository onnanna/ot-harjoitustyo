# luokka joka kuvaa yksittäistä elokuvaa
import uuid

class Movies:

    def __init__(self, title, year, seen=False, user=None, movie_id=None, stars:int=0):
        self.title = title
        self.year = year
        self.seen = seen
        self.user = user
        self.id = movie_id if movie_id else str(uuid.uuid4())
        self.stars = stars
