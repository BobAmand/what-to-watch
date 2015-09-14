import csv

all_movies = {}
all_users = {}

class User:
    def __init__(self, user_id):
        self.uid = user_id
        # self.age = age
        # self.occ = occupation
        # self.tms = timestamp
        all_users[self.uid] = self  # dict with key = user_id
        self.ratings = {}

    def get_user_data():
        with open('u.user', encoding='latin_1') as f:
            user_reader = csv.DictReader(f, fieldnames=['user_id',
                                            'age',
                                            'gender',
                                            'occupation',
                                            'zipcode',
                                            ]
                                            ,delimiter='|')
        return user_reader

    def add_rating(self, rating):   #loads the user_id and rating to rating
        self.ratings[rating.uid] = rating       # duplicate from Movie yet operates locally

    def get_ratings(self):          #gets the ratings by user_id
        return self.ratings.values()

    def get_ave_rating(self):       # gets average rating by user_id
        return sum(get_ratings(self))/len(get_ratings(self))

    def __str__(self):
        return 'User(user_id={})'. format(self.uid)

    def __repr__(self):
        return self.__str__()

class Movie:
    def __init__(self, movie_id, title):
        self.mid = movie_id
        self.tid = title
        all_movies[self.mid] = self # dict with key=movie_id, value=title
        self.ratings = {} #key is user_id, value: Rating object = rating dictionary

    def get_movie_data():
        with open('u.item', encoding='latin_1') as f:
            item_reader = csv.DictReader(f, fieldnames=['m_id','m_title'],delimiter='|')
        return item_reader

    def add_rating(self, rating):   # loads the user_id and rating to ratings dict
        self.ratings[rating.uid] = rating   #user_id is key

    def get_ratings(self):          # gets the ratings by user_id
        return self.ratings.values()

    def get_ave_rating(self):       # gets average rating by movie
        return sum(get_ratings(self))/len(get_rating(self))

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
        all_users[self.uid].add_rating(self)

    def get_rating_data():
        with open('u.data', encoding='latin_1') as f:
            data_reader = csv.DictReader(f, fieldnames=['user_id',
                                            'movie_id',
                                            'rating',
                                            ]
                                            ,delimiter='\t')
        return data_reader

    def __str__(self):
        return 'Rating(user_id={}, movie_id={}, stars={})'. format(self.uid, self.mid, self.sid)

    def __repr__(self):
        return self.__str__()
