# test script - What to Watch
#import unittest
from movie_lib import *

user1 = User(666)     #note User(), refers to class User object.
user2 = User(123)
user3 = User(99)
user4 = User(0)
movie1 = Movie(23, 'The Matrix')    #Two parameterss
movie2 = Movie(45, 'Toy Story')
rating1 = Rating('B', 45, 3)        #Three parameters
rating2 = Rating(123, 45, 5)
rating3 = Rating(user1.uid, movie2.mid, 1)
rating4 = Rating(user2.uid, movie2.mid, 5)


def test_user_creation():
    assert user1.uid == 666
    assert user2.uid == 123
    assert user3.uid == 99
    assert user4.uid == 0

def test_movie_creation(): # takes 2 parameters: movie_id, title
    assert movie1.mid == 23
    assert movie1.tid == 'The Matrix'
    assert movie2.mid == 45
    assert movie2.tid =='Toy Story'

def test_rating_creation(): # takes 3 parameters: user_id, movie_id, star
    assert rating1.uid == 'B'
    assert rating1.mid == 45
    assert rating1.sid == 3
    assert rating2.uid == 123
    assert rating2.mid == 45
    assert rating2.sid == 5
    assert rating3.uid == 666
    assert rating3.mid == 45
    assert rating3.sid == 1
    assert rating4.uid == 123
    assert rating4.mid == 45
    assert rating4.sid == 5
