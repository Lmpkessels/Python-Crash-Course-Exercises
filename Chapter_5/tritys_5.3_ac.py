### Excersise 5-3, Alien Colors #1 ###

# Telling what color the alien is
alien_color = "green"

# What to do if the color of the alien is green
if alien_color == "green":
    print("You have earned 5 points!")

# Telling what the other alien his color is
alien_color = "yellow"

# Putting out nothing because the value isn't the same as the value
# assigned to the variable above.
#
# Telling what the other alien his color is
if alien_color == "brown":
    print("You have earned 5 points!")


### Excersise 5-4, Alien Colors #2 ###

# Telling the program what color the alien is
alien_color = "green"

# Telling the user how many points he/she has earned by shooting down
# the green alien.
if alien_color == "green":
    print("You have earned 5 points!")
else:
    print("You have earned 10 points!")


# Telling what color the alien is
alien_color = "purple"

# Telling the user how many points he/she has earned by shooting down
# on of the other aliens.
if alien_color == "green":
    print("You have earned 5 points!")
else:
    print("You have earned 10 points!")


"""
Above you have executed excersise 5-3 Alien Colors #1, and excersise
5-4, Alien Colors #2. Now today - Finish 5-5, Alien Colors #3, 
5-6, Stages of Life, and 5-7, Favorite Fruit.

Good Luck! :)
"""

### Excersise 5-5, Alien Colors #3 ###


# Program for shooting down a green alien
alien_color = "green"

# Telling the user he/she has earned 5 points
if alien_color == "green":
    print("\nYou have earned 5 points!")
elif alien_color == "yellow":
    print("\nYou have earned 10 points!")
elif alien_color == "red":
    print("\nYou have earned 15 points!")


# Program for shooting down a yellow alien
alien_color = "yellow"

# Telling the user he/she has earned 10 points
if alien_color == "green":
    print("\nYou have earned 5 points!")
elif alien_color == "yellow":
    print("\nYou have earned 10 points!")
elif alien_color == "red":
    print("\nYou have earned 15 points!")


# Program for shooting down a red alien
alien_color = "red"

# Telling the user he/she has earned 15 points
if alien_color == "green":
    print("\nYou have earned 5 points!")
elif alien_color == "yellow":
    print("\nYou have earned 10 points!")
elif alien_color == "red":
    print("\nYou have earned 15 points!")


### Excersis 5-6, Stages of Life ###


# Determing stage of life
person = 13

# Declaring what stage of life the person is based on the data we gather
#
# For every stage of life a message get's printed to the user
if person < 2:
    print("\nThe person is a baby.")
elif person < 4:
    print("\nThe person is a toddler.")
elif person < 13:
    print("\nThe person is a kid.")
elif person < 20:
    print("\nThe person is a teenager.")
elif person < 65:
    print("\nThe person is an adult.")
else:
    print("\nThe person is an elder.")


### Excersise 5-6, Stages of Life ###


# Three of my favorite fruits
favorite_fruits = ["blueberry", "strawberry", "raspberry"]

# Checking if in list
in_list = "apple"


# Telling the user if blueberry's are in the list of my favorite fruits
# and how much I like them.
if "blueberry" in favorite_fruits:
    print("\nBlueberry is in the list.")
    print("I really like blueberry's!")

# Telling the user if strawberry's are in the list of my favorite fruits
# and how much I like them.
if "strawberry" in favorite_fruits:
    print("\nStrawberry is in the list.")
    print("I really like Strawberry's!")

# Telling the user if raspberry's are in the list of my favorite fruits
# and how much I like them.
if "raspberry" in favorite_fruits:
    print("\nRaspberry is in the list.")
    print("I really like Raspberry's!")

# Telling the user that if raspberry's and blueberry's are in the list
# of my favorite foods, then they should be bought at the suppermarket.
if "raspberry" in favorite_fruits and "blueberry":
    print("\nBuy raspberry's and blueberry's in the supermarket.")

# Telling the user to not buy apples because I don't like apple's
if in_list not in favorite_fruits:
    print("\nDon't buy apple's")
    print("I don't like apple's")


