# test script - What to Watch
from movie_lib.py import *

'''
test data:
     A dictionary for ratings by movie.
'''
# uid dictionary: {key = uid: value: movieid}
uid = {11:[400 ,404 ,410], 22:[400, 410 ,440], 33:[440, 404 ,410]}

# movieid = [400, 440, 404, 410]
# movie matrix:     uid  movieid rating
movie_rate_matrix = [[11, 400, 5],
                     [11, 404, 3],
                     [11, 410, 2],
                     [22, 400, 6],
                     [22, 410, 7],
                     [22, 440, 5],
                     [33, 440, 1],
                     [33, 404, 2],
                     [33, 410, 1]
                     ]

def User(self, uid):
    AssertTrue(self.userid(11))=[5, 3, 2]
    AssertTrue(self.userid(33))=[1, 2, 2]
    AssertFalse(self.userid(33))=[6, 7, 5]
