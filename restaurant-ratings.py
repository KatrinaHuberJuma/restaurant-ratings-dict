# your code goes here
""" Reads the ratings in from the file
Stores them in a dictionary, and then
Spits out the ratings in alphabetical order by restaurant """

def display_ratings(filepath):
    """Takes a file with multiple lines and spits out names and ratings of restaurants in alphabetical order."""

    open_file = open(filepath)

    restaurants_and_ratings = {}

    for line in open_file:
        restaurant, rating = line.split(":")
        restaurants_and_ratings[restaurant] = rating

    alphabetized_keys = sorted(restaurants_and_ratings.keys())

    for key in alphabetized_keys:
        print key, "is rated", restaurants_and_ratings[key]


display_ratings("scores.txt")