# test script - What to Watch
#import unittest
from movie_lib import *


def test_user_creation():
    user1 = User('A')     #note User(), refers to class User object.
    user2 = User(123)
    user3 = User(99)
    user4 = User(0)
    assert user1.uid == 'A'
    assert user2.uid == 123
    assert user3.uid == 99
    assert user4.uid == 0

def test_movie_creation(): # takes 2 parameters: movie_id, title
    movie1 = Movie(23, 'The Matrix')
    movie2 = Movie(45, 'Toy Story')
    assert movie1.mid == 23
    assert movie1.tid == 'The Matrix'
    assert movie2.mid == 45
    assert movie2.tid =='Toy Story'

def test_rating_creation(): # takes 3 parameters: user_id, movie_id, star
    rating1 = Rating('A', 45, 3)
    rating2 = Rating(123, 45, 5)
    assert rating1.uid == 'A'
    assert rating1.mid == 45
    assert rating1.sid == 3
    assert rating2.uid == 123
    assert rating2.mid == 45
    assert rating2.sid == 5
