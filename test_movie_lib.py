# test script - What to Watch
#import unittest
from movie_lib import *


def test_user_creation():
    user1 = User(5)
    assert user1.uid == 5

def test_movie_creation():
    movie1 = Movie(23, 'The Matrix')
    assert movie1.mid == 23
    assert movie1.tid == 'The Matrix'

def test_rating_creation():





# def test_movie_creation():
#     movie1 = Movie(3, 'Toy Story')
#     assert movie1.mid == 3
#     assert movie1.mid == 'Toy Story'
