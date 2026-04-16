# Program to store and display details of 3 movies

movies = {}  # main dictionary

for i in range(1, 4):
    print(f"\nEnter details for Movie {i}")
    
    title = input("Title: ")
    director = input("Director: ")
    year = input("Release Year: ")
    rating = input("Rating (out of 10): ")
    
    # storing each movie as a nested dictionary
    movies[i] = {
        "Title":title,
        "Director": director,
        "Release Year": year,
        "Rating": rating
    }


print("\n\n MOVIE DETAILS \n")

for key, movie in movies.items():
    print(f"Movie {key}")
    print(f"Title        : {movie['Title']}")
    print(f"Director     : {movie['Director']}")
    print(f"Release Year : {movie['Release Year']}")
    print(f"Rating       : {movie['Rating']}/10")
    print("-" * 30)