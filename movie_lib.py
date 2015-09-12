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
    def __init__(self, user_id, movie_id, star):
        self.uid = user_id
        self.mid = movie_id
        self.sid = star
