# your code goes here
""" Reads the ratings in from the file
Stores them in a dictionary, and then
Spits out the ratings in alphabetical order by restaurant

Choose a random restaurant from the list in the file (hint: the choice() function in the Random module will probably come in handy here)
Tell the user the chosen restaurant and its rating
Ask the user what the new rating should be
Update the rating

"""
import random


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

    random_restaurant_name = random.choice(alphabetized_keys)

    restaurants_and_ratings[random_restaurant_name] = raw_input("the rating of %s is %s, what should the new rating be? " % (random_restaurant_name, restaurants_and_ratings[random_restaurant_name]))

    for key in alphabetized_keys:
        print key, "is rated", restaurants_and_ratings[key]

    open_file.close()



def adds_new_restaurant(established_restaurants):
    user_added_restaurant = raw_input("Enter a new restaurant ")
    user_added_rating = int(raw_input("Enter that restaurant's rating "))
    established_restaurants[user_added_restaurant] = user_added_rating

display_ratings("scores.txt")