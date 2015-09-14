import csv
 '''
  TODO: import the data at the appropriate point:
    1. stopped working with data imports to refocus on the functions to
        solve:

 '''
with open('u.item', encoding='latin_1') as f:
    item_reader = csv.DictReader(f, fieldnames=['m_id','m_title'],delimiter='|')
    for row in item_reader:
        print(row)

with open('u.item', encoding='latin_1') as f:
    item_reader = csv.reader(f, delimiter='|')
    for row in item_reader:
        print(row)


with open('u.data', encoding='latin_1') as f:
    data_reader = csv.DictReader(f, fieldnames=['user_id',
                                            'movie_id',
                                            'rating',
                                            ]
                                            ,delimiter='\t')
    for row in data_reader:
        print(row)

with open('u.user', encoding='latin_1') as f:
    user_reader = csv.DictReader(f, fieldnames=['user_id,
                                            'age',
                                            'gender',
                                            'occupation',
                                            'zipcode',
                                            ]
                                            ,delimiter='|')
    for row in user_reader:
        print(row)

all_movies = {}
all_users = {}

class User:
    def __init__(self, user_id):
        self.uid = user_id
        # self.age = age
        # self.occ = occupation
        # self.tms = timestamp
            # will eventually add age, occupation, timestamp
        all_users[self.uid] = self  # dict with key = user_id

    def get_rating(self, rating):


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

    def add_rating(self, rating):   # loads the user_id and rating to ratings dict
        self.ratings[rating.uid] = rating   #user_id is key

    def get_ratings(self):          # gets the ratings by user_id
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
        all_users[self.uid].add_rating(self)

    def __str__(self):
        return 'Rating(user_id={}, movie_id={}, stars={})'. format(self.uid, self.mid, self.sid)

    def __repr__(self):
        return self.__str__()

# def all_ratings_by_movie_by_id(all_movies):
#     for i in all_movies:
