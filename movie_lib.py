
all_movies = {}
all_users = {}

class User:
    def __init__(self, user_id):
        self.uid = user_id
        all_users[self.uid] = self

class Movie:
    def __init__(self, movie_id, title):
        self.mid = movie_id
        self.tid = title
        all_movies[self.mid] = self
        self.ratings = {} #key is user_id, value: Rating object

    def add_rating(self, rating):
        self.ratings[rating.uid] = rating   #user_id is key

    def get_ratings(self):
        return self.ratings.values()

    def __str__(self):          # a string representation of Movie() class
        return 'Movie(movie_id={}, title={})'. format(self.mid, repr(self.tid))

    def __repr__(self):         # brings the string representation into dict
        return self.__str__()

class Rating:
    def __init__(self, user_id, movie_id, star):
        self.uid = user_id
        self.mid = movie_id
        self.sid = star
        all_movies[self.mid].add_rating(self)

    def __str__(self):
        return 'Rating(user_id={}, movie_id={}, stars={})'. format(self.uid, self.mid, self.sid)

    def __repr__(self):
        return self.__str__()
