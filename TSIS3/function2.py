# 1. Write a function that takes a single movie and returns True if its IMDB score is above 5.
from movies import movies

def is_movie_good(movies ,movie_name):
    curr_movie = dict(())
    for movie in movies:
        if movie["name"] == movie_name:
            curr_movie = movie
    return curr_movie["imdb"] > 5.5


print(is_movie_good(movies, "Hitman"))

# 2. Write a function that returns a sublist of movies with an IMDB score above 5.5.

def get_good_movies(movies):
    good_movies = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            good_movies.append(movie["name"])
    return good_movies

print(get_good_movies(movies))

# 3. Write a function that takes a category name and returns just those movies under that category.

def get_movies_by_category( movies, category):
    movies_list = []
    for movie in movies:
        if movie['category'] == category:
            movies_list.append(movie)
    return movies_list

print(get_movies_by_category(movies, "Drama"))
print(get_movies_by_category(movies, "Suspense"))

# 4. Write a function that takes a list of movies and computes the average IMDB score.

def get_average_rating(movies):
    sum = 0
    num_movies = len(movies)
    for movie in movies:
        sum += movie["imdb"]
    return sum/num_movies

print(get_average_rating(movies))

# 5. Write a function that takes a category and computes the average IMDB score.
def get_avg_rating_by_category(movies, category):
    sum = 0
    num_movies = 0
    for movie in movies:
        if movie['category'] == category:
            sum += movie['imdb']
            num_movies += 1
    return sum / num_movies

print(get_avg_rating_by_category(movies, 'Suspense'))