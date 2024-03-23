import math


def compute_recom(movies, movie_rec):
    eucl_arr = []

    for movie in movies:
        eucl_arr.append(compute_euclidean(movie, movie_rec))

    min_index = eucl_arr.index(min(eucl_arr))

    if movies[min_index].pop() > 7:
        return True
    else:
        return False


def compute_euclidean(movie, movie_rec):
    result = 0

    for i in range(len(movie_rec)):
        result += math.pow(movie[i] - movie_rec[i], 2)

    return math.sqrt(result)


# Je Array: [Horror, Romantik, Humor, Userbewertung]
movieA = [2, 4, 6, 8]
movieB = [8, 2, 1, 2]
movieC = [2, 3, 8, 9]
movies = [movieA, movieB, movieC]

movie_rec = [5, 4, 9]

print(compute_recom(movies, movie_rec))
