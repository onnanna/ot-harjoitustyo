import uuid

class Movies:
    """Luokka, joka kuvaa yksittäistä elokuvaa
    Attributes:
        title: Merkkijonoarvo, joka kuvaa elokuvan nimeä
        year: Merkkijonoarvo, joka kuvaa elokuvan julkaisuvuotta
        seen: Boolean-arvo, joka kuvastaa onko elokuvaa vielä nähty
        user: User-olio, joka kuvaa elokuvan omistajaa
        movie_id: Merkkijonoarvo, joka kuvaa elokuvan id:tä
        stars: Merkkijonoarvo, joka kuvaa elokuvan tähtiarviota
        genre: Merkkijonoarvo, joka kuvaa elokuvan genreä
        notes: Merkkijonoarvo, joka kuvaa elokuvan lisätietoja
        """
    
    def __init__(self, title, year, seen=False, user=None, movie_id=None, stars:int=0, genre=None, notes=None):
        """Luokan konstruktori, joka luo uuden elokuvan

        Args:
            title: Merkkijonoarvo, joka kuvaa elokuvan nimeä
            year:
                Vapaaehtoinen, oletusarvoltaan None
                Merkkijonoarvo, joka kuvaa elokuvan julkaisuvuotta
            seen:
                Vapaaehtoinen, oletusarvoltaan False
                Boolean-arvo, joka kuvastaa onko elokuvaa vielä nähty
            user:
                Vapaaehtoinen, oletusarvoltaan None
                User-olio, joka kuvaa elokuvan omistajaa
            movie_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid
                Merkkijonoarvo, joka kuvaa elokuvan id:tä
            stars:
                Vapaaehtoinen, oletusarvoltaan 0
                Kokonaisluku, joka kuvaa elokuvan tähtiarviota
            genre:
                Vapaaehtoinen, oletusarvoltaan None
                Merkkijonoarvo, joka kuvaa elokuvan genreä
            notes:
                Vapaaehtoinen, oletusarvoltaan None
                Merkkijonoarvo, joka kuvaa elokuvan lisätietoja
        """
        self.title = title
        self.year = year
        self.seen = seen
        self.user = user
        self.id = movie_id if movie_id else str(uuid.uuid4())
        self.genre = genre
        self.notes = notes
        self.stars = stars
