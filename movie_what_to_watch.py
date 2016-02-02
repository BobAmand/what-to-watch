from movie_lib import *
from movie_lib_user import *

'''
With help from Andrew Pierce.
'''


def top_50():
    popularity = {}
    for key, value in all_ratings.items():
        if len(value) >= 20:   # more than 20 raters
            avg = sum(value)/len(value)
            popularity[key] = round(avg, 2)  # 2 decimals in average
            sorted_list = sorted(popularity.items(), key=lambda c: c[1], reverse=True)
            top_50 = sorted_list[:50]
            counter = 0
    for x in top_50:
        print(str(counter+1) + ': ' + str(all_movies[top_50[counter][0]]) + ' ' + str(top_50[counter][1]))
        counter += 1


def top_50_for_user(user_id):
    pop_unseen = {}
    user_seen = all_reviewed(user_id)
    for key, value in all_ratings.items():
        if key not in user_seen:
            if len(value) >= 20:
                avg = sum(value)/len(value)
                pop_unseen[key] = round(avg, 2)
                sorted_list = sorted(pop_unseen.items(), key=lambda c: c[1], reverse=True)
                top_50 = sorted_list[:50]
                counter = 0
    for x in top_50:
        print(str(counter+1) + ': ' + str(all_movies[top_50[counter][0]]) + ' ' + str(top_50[counter][1]))
        counter += 1


def rec_for_user(user_id):
    sim_users = find_sim_users(user_id)   # similar user_seen
    seen_movies = all_reviewed(user_id)
    rec_movies = []
    for x in sim_users:
        sim_movies = all_reviewed(x)
        for movie in sim_movies:
            if movie not in seen_movies:
                if all_users[x][movie] >= 5:
                    rec_movies.append(movie)
    counter = 1
    rec_movies = list(set(rec_movies))
    for x in rec_movies:
        print(str(counter) + ': ' + str(all_movies[x]))
        counter += 1
    if len(rec_movies) == 0:
        print("You are unique. No similar users!")
        print("Here are the Top 50 movies you haven't seen:")
        top_50_for_user(user_id)


def main():
    print("Here are the best movies in Movie Lens...")
    response = input("What do you want to see? "
                     + "[1] for overall top 50, "
                     + "[2] for top 50 you haven't seen, or "
                     + "[3] for recommended movies.\n"
                     )

    if response == '1':
        top_50()
    elif response == '2':
        user = input("What is your id?  We have total of 943 users. \n")
        user = int(user)
        top_50_for_user(user)
    elif response == '3':
        user = input("What is your id?  We have total of 943 users. \n")
        user = int(user)
        rec_for_user(user)
    else:
        print("Enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
