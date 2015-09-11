# test script - What to Watch
import unittest
from movie_lib import *

'''
test data:
     A dictionary for ratings by movie.
'''
# uid dictionary: {key = uid: value: useridmovieid}
udict = {11:User(400), 22:User(410), 33:User(440)}
# uid dictionary: {key = uid: value: movieid}
# uid_dict = {11:[400 ,404 ,410], 22:[400, 410 ,440], 33:[440, 404 ,410]}
# # movieid = [400, 440, 404, 410]
# # movie matrix:     uid  movieid rating
# movie_rate_matrix = [[11, 400, 5],
#                      [11, 404, 3],
#                      [11, 410, 2],
#                      [22, 400, 6],
#                      [22, 410, 7],
#                      [22, 440, 5],
#                      [33, 440, 1],
#                      [33, 404, 2],
#                      [33, 410, 1],
#                      ]
uid = 11
class testUser(self, uid):
    self.assertTrue(udict[uid].userid, 400) # should be True
    # self.assertTrue(self.userid(33) == [1, 2, 2])  # should be True
    # self.assertFalse(self.userid(33) == [6, 7, 5]) # should be False
