# test script - What to Watch
# import unittest
from movie_lib import *

user1 = User(123)     #note User(), refers to class User object.
user2 = User(456)
user3 = User(99)
user4 = User('A')
movie1 = Movie(23, 'The Matrix')    #Two parameterss
movie2 = Movie(45, 'Toy Story')
rating1 = Rating(123, 23, 3)        #Three parameters
rating2 = Rating(456, 23, 5)
rating3 = Rating(user1.uid, movie2.mid, 1)
rating4 = Rating(user2.uid, movie2.mid, 5)

print(all_movies)   # passes all movies into dictionary
print(all_movies[45])   # passes one movie into the dictionary
print(all_movies[23])
print(id(movie2))   #'the id() function reveals memory location'
print(id(all_movies[45]))  # passes in all_movies[self.mid]
                    # The above will show the same memory location!

def test_user_creation():
    assert user1.uid == 123
    assert user2.uid == 456
    assert user3.uid == 99
    assert user4.uid == 'A'

def test_movie_creation(): # takes 2 parameters: movie_id, title
    assert movie1.mid == 23
    assert movie1.tid == 'The Matrix'
    assert movie2.mid == 45
    assert movie2.tid =='Toy Story'

def test_rating_creation(): # takes 3 parameters: user_id, movie_id, star
    assert rating1.uid == 123
    assert rating1.mid == 23
    assert rating1.sid == 3
    assert rating2.uid == 456
    assert rating2.mid == 23
    assert rating2.sid == 5
    assert rating3.uid == 123
    assert rating3.mid == 45
    assert rating3.sid == 1
    assert rating4.uid == 456
    assert rating4.mid == 45
    assert rating4.sid == 5

def test_find_ratings_for_movie():
    #toy_story_ratings = get_ratings_for_movie(movie2.mid)
        # alternative approaches
    # Return a list of Rating objects
    toy_story_ratings = all_movies[movie2.mid].get_ratings()
    print(len(toy_story_ratings))
    print(toy_story_ratings)
    assert len(toy_story_ratings) == 2   #Two users rated movieToystory

def test_find_user():
    user_one = all_users[user1.uid].get_ratings()
    print(len(all_users))
    print(all_users)
    assert len(all_users) == 4  # Four total users id in test data

def test_find_ratings_by_user():
    user_one_ratings = all_users[user1.uid].get_ratings()
    print(len(user_one_ratings))
    print(user_one_ratings)
    assert len(user_one_ratings) == 1
