# your code goes here
""" Reads the ratings in from the file
Stores them in a dictionary, and then
Spits out the ratings in alphabetical order by restaurant
"""

def display_ratings(filepath):
    """Takes a file with multiple lines and spits out names and ratings of restaurants in alphabetical order."""

    open_file = open(filepath)

    restaurants_and_ratings = {}

    adds_new_restaurant(restaurants_and_ratings)

    for line in open_file:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        restaurants_and_ratings[restaurant] = rating

    alphabetized_keys = sorted(restaurants_and_ratings.keys())

    for key in alphabetized_keys:
        print key, "is rated", restaurants_and_ratings[key]

    open_file.close()



def adds_new_restaurant(established_restaurants):
    user_added_restaurant = raw_input("Enter a new restaurant ")
    user_added_rating = int(raw_input("Enter that restaurant's rating "))
    established_restaurants[user_added_restaurant] = user_added_rating

display_ratings("scores.txt")