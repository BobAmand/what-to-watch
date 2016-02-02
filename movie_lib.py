import csv
'''
with help from Andrew Pierce.
note the read of u.item for movie data.
'''
with open("ml-100k/u.item", encoding='latin_1') as f:
    all_movies = {}
    reader1 = csv.reader(f, delimiter='|')
    for row in reader1:
        key = int(row[0])
        all_movies[key] = row[1]  # assigns title to each key in first column.

'''
note the next read is of u.data for the ratings.
'''
with open("ml-100k/u.data", encoding='latin_1') as f:
    all_ratings = {}
    reader1 = csv.reader(f, delimiter='\t')
    for row in reader1:
        key = int(row[1])
        if key not in all_ratings:
            all_ratings[key] = list(row[2])
        else:
            all_ratings[key].append(row[2])
    all_ratings = {k:[int(x) for x in values] for k,values in all_ratings.items()}

'''
note the next read is of u.data for the user.
the file u.user is not needed at this point.
'''
with open("ml-100k/u.data", encoding='latin_1') as f:
    all_users = {}
    reader1 = csv.reader(f, delimiter='\t')
    for row in reader1:
        if key not in all_users:
            all_users[key] = {int(row[1]): int(row[2])}
        else:
            all_users[key].update({int(row[1]): int(row[2])})




class User:
    def __init__(self, user_id):
        self.uid = user_id
        # self.age = age
        # self.occ = occupation
        # self.tms = timestamp
        all_users[self.uid] = self  # dict with key = user_id
        # self.ratings = {}

    def all_ratings(self):
        return all_users[self.id]

    # def get_user_data():
    #     with open('u.user', encoding='latin_1') as f:
    #         user_reader = csv.DictReader(f, fieldnames=['user_id',
    #                                         'age',
    #                                         'gender',
    #                                         'occupation',
    #                                         'zipcode',
    #                                         ]
    #                                         ,delimiter='|')
    #     return user_reader
    #
    # def add_rating(self, rating):   #loads the user_id and rating to rating
    #     self.ratings[rating.uid] = rating       # duplicate from Movie yet operates locally
    #
    # def get_ratings(self):          #gets the ratings by user_id
    #     return self.ratings.values()
    #
    # def get_ave_rating(self):       # gets average rating by user_id
    #     return sum(get_ratings(self))/len(get_ratings(self))
    #
    # def __str__(self):
    #     return 'User(user_id={})'. format(self.uid)
    #
    # def __repr__(self):
    #     return self.__str__()

class Movie:
    def __init__(self, movie_id, title=None, ratings=None):
        self.id = movie_id
        self.title = all_movies[self.id]
        self.ratings = all_ratings[self.id]
        all_movies[self.id] = self # dict with key=movie_id, value=title
        all_ratings[self.id] = self # key is user_id, value: Rating object = rating dictionary
    #
    # def get_movie_data():
    #     with open('u.item', encoding='latin_1') as f:
    #         item_reader = csv.DictReader(f, fieldnames=['m_id','m_title'],delimiter='|')
    #     return item_reader
    #
    # def add_rating(self, rating):   # loads the user_id and rating to ratings dict
    #     self.ratings[rating.uid] = rating   #user_id is key
    #
    # def get_ratings(self):          # gets the ratings by user_id
    #     return self.ratings.values()
    #
    # def get_ave_rating(self):       # gets average rating by movie
    #     return sum(get_ratings(self))/len(get_rating(self))

    def __str__(self):          # a string representation of Movie() class
        return 'Movie: movie_id = {}, title = {}, ratings = {})'. format(self.id, repr(self.title), repr(self.ratings))

    def __repr__(self):         # brings the string representation into dict
        return self.__str__()

class Rating:
    def __init__(self, user_id, movie_id, stars):
        self.user = user_id
        self.movie = movie_id
        self.stars = stars
    #
    #     all_movies[self.mid].add_rating(self)
    #     all_users[self.uid].add_rating(self)
    #
    # def get_rating_data():
    #     with open('u.data', encoding='latin_1') as f:
    #         data_reader = csv.DictReader(f, fieldnames=['user_id',
    #                                         'movie_id',
    #                                         'rating',
    #                                         ]
    #                                         ,delimiter='\t')
    #     return data_reader

    def __str__(self):
        return 'Rating(user_id={}, movie_id={}, stars={})'. format(self.user, self.movie, self.stars)

    def __repr__(self):
        return self.__str__()

    def avg_rating(self):
        avg = round(sum(self.ratings)/len(self.ratings), 2)
        return avg
    # movie1 = input("What movie would you like to see ratings?: ")
