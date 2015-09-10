# movie_lib.py
# This will contain my classes
#
class User:
    def __init__(self, uid):
        self.userid = uid

class Movie(User):
    def __init__(self, movieid, uid):
        self.movieid = movieid
        self.userid = uid

class Rating(User):
    def __init__(self, rating, movieid, uid):
        self.rating = rating
        self.movieid = movieid
        self.userid = uid
