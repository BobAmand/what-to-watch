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
            top_50a = sorted_list[:10]   # Top 10
            counter = 0
    for x in top_50a:
        print(str(counter+1) + ': ' + str(all_movies[top_50a[counter][0]]) + ' ' + str(top_50a[counter][1]))
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
                top_50 = sorted_list[:10]  # top 10
                counter = 0
    for x in top_50:
        print(str(counter+1) + ': ' + str(all_movies[top_50[counter][0]]) + ' ' + str(top_50[counter][1]))
        counter += 1


def rec_for_user(user_id):
    sim_users = find_sim_users(user_id)   # similar user_seen
    print("Similar user_ids are: {}\n".format(sim_users))
    seen_movies = all_reviewed(user_id)
    rec_movies = []
    for x in sim_users:
        sim_movies = all_reviewed(x)
        for movie in sim_movies:
            if movie not in seen_movies:
                if all_users[x][movie] >= 5:
                    rec_movies.append(movie)
    counter = 1
    rec_movies = list(set(rec_movies))[:10]   # first 10 in list
    for x in rec_movies:
        print(str(counter) + ': ' + str(all_movies[x]))
        counter += 1
    if len(rec_movies) == 0:
        print("You are unique. No similar users!")
        print("Here are the Top 10 movies you haven't seen:")
        top_50_for_user(user_id)


def main():
    print("Here are the best movies in Movie Lens...")
    response = input("What do you want to see? \n"
                     + "   Select [1] for overall top 10, \n"   # top 50
                     + "   Select [2] for top 10 you haven't seen, or \n"
                     + "   Select [3] for recommended movies for you.\n\n"
                     )

    if response == '1':
        print("You selected 1, here is the top 50 (10): \n")
        top_50()
    elif response == '2':
        user = input("What is your id?  We have total of 943 users. \n")
        user = int(user)
        print("Your id is: {}, here are the Top 10 movies you have not seen: \n".format(user))
        top_50_for_user(user)
    elif response == '3':
        user = input("What is your id?  We have total of 943 users. \n")
        user = int(user)
        print("Here are 10 recommended movies: \n")
        rec_for_user(user)
    else:
        print("Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
