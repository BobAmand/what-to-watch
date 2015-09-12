# movie_lib.py
# This will contain my classes
#
class User:
    def __init__(self, user_id):
        self.uid = user_id

class Movie:
    def __init__(self, movie_id, title):
        self.mid = movie_id
        self.tid = title

class Rating:
    def __init__(self, star, movie_id, user_id):
        self.sid = star
        self.mid = movie_id
        self.uid = user_id
