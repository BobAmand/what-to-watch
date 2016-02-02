from movie_lib import *
import math

'''
With help from Andrew Pierce.
'''


def all_reviewed(user_id):
    movies_seen = []
    safe_copy = all_users[user_id]
    [movies_seen.append(x) for x in safe_copy]
    sorted_movies_seen = sorted(movies_seen)
    return sorted_movies_seen


def compare_users(user1_id, user2_id):
    '''creates list of commonly viewed movies'''
    user1_movies = all_reviewed(user1_id)
    safe_copy1 = user1_movies[:]
    user2_movies = all_reviewed(user2_id)
    safe_copy2 = user2_movies[:]
    shared = []
    [shared.append(x) for x in safe_copy1 if x in safe_copy2]
    return shared


def selected_ratings(movie_list, user):
    select_ratings = []
    safe_copy = movie_list
    [select_ratings.append(x[1]) for x in all_users[user].items() if x[0] in safe_copy]
    return select_ratings


def euclidian_distance(user1, user2):
    shared = compare_users(user1, user2)
    ratings_a = selected_ratings(shared, user1)
    ratings_b = selected_ratings(shared, user2)
    differences = [ratings_a[x] - ratings_b[x] for x in range(len(ratings_a))]
    squares = [diff**2 for diff in differences]
    sum_of_squares = sum(squares)
    return 1 / (1 + math.sqrt(sum_of_squares))


def find_sim_users(user):
    similar_users = []
    counter = 1
    for x in range(943):
        if counter != user:
            sim = euclidian_distance(user, counter)
            if sim == 1.0 or sim == .50:
                continue
            if sim >= .16:
                similar_users.append(counter)
        counter += 1
    return similar_users
