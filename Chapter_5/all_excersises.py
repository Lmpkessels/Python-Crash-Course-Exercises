# Declaring an age then testing age with a conditional to see if, its
# True or False.
age = 24
print(age == 24, "I predict is True")
print(age == 25, "I predict is False")


# 10 Tests to evaluate True or False of which 5 are True and 5 are False
customer_name = "Luuk"
print(customer_name == "Luuk", "I predict is True")
print(customer_name == "Luuk Kessels", "I predict is False")
print(customer_name != "Luuk", "I predict is False")

book = "The Law of Success"
print(book == "The Law of Success", "I predict is True")
print(book == "The Art of Clear Thinking", "I predict is False")
print(book != "The Law of Success", "I predict is False")

favorite_sports = "Kickboxing and Weightlifting"
print(favorite_sports == "Kickboxing and Weightlifting", "I predict is"
" True")
print(favorite_sports == "Horse riding", "I predict is False")
print(favorite_sports != "Kixkbozing and Weightlifting", "I predict is" 
" False")

programming_language = "Python"
print(programming_language == "Python", "I predict is True")
print(programming_language == "JavaScript", "I predict is False")
print(programming_language != "Python", "I predict is False")

cow = "White with Black"
print(cow == "White with Black", "I predict is True")
print(cow == "Purple", "I predict is False")
print(cow != "White and Black", "I predict is False")


# Looking at the equality and inequality with strings
string = "string"
print(string == "string", "I predict is True")
print(string == "not string", "I predict is False")

# Testing True or False using the .lower function
name = "Koen"
print(name.lower() == "koen", "I predict is True")
print(name.lower() == "Koen", "I predict is False")

# Testing equality and inequality in numbers
number = 24
print(number > 24, "I predict is False")
print(number < 24, "I predict is False")
print(number >= 24, "I predict is True")
print(number <= 24, "I predict is True")

# Testing using AND keyword
name = "Luuk"
last_name = "Kessels"
print(name == "Luuk" and last_name == "Kessels", "I predict is True")

num = 29
print(num <= 30 and num >= 20, "I predict is True")


# Testing using OR keyword
plant = "green"
print(plant == "green" or plant == "yellow", "I predict is True")

numb = 300
print(numb <= 300 or numb >= 400, "I predict is True")


# Testing if item is IN list
items_in_list = ["book", "pen", "journal", "etui"]
print("pen" in items_in_list, "I predict is True")

# Checking if item IS NOT in list
print("book" not in items_in_list, "I predict is False")

#______________________________________________________________________#

# Declaring alien color in video game
alien_color = "green"

# Telling program what to do when alien color green is shot down
#
# Note a if...else.... statement keeps going till a value is meat to be
# True, if False it will go to the else.
if alien_color == "green":
    print("You have earned 5 points!")
else:
    print("This will do nothing")

# Declaring color of alien in video game
alien_color = "green"

# Using a if else chain to tell the program what to do when the value 
# is met.
if alien_color == "green":
    print("You have earned 5 points!")
else:
    print("You have earned 10 points!")

# This program returns the else statement
alien_color = "red"

if alien_color == "green":
    print("You have earned 5 points!")
else:
    print("You have earned 10 points!")

# This program return the points of shooting down a green alien
# Declaring color of alien in video game
alien_color = "green"

# Using a if else chain to tell the program what to do when the value 
# is met.
#
# Asigning points to the alien color; green, yellow, and red
if alien_color == "green":
    print("You have earned 5 points!")
elif alien_color == "yellow":
    print("You have earned 10 points!")
elif alien_color == "red":
    print("You have earned 15 points!")

# This program return the points of shooting down a yellow alien
# Declaring color of alien in video game
alien_color = "yellow"

# Asigning points to the alien color; green, yellow, and red
if alien_color == "green":
    print("You have earned 5 points!")
elif alien_color == "yellow":
    print("You have earned 10 points!")
elif alien_color == "red":
    print("You have earned 15 points!")

# This program return the points of shooting down a red alien
# Declaring color of alien in video game
alien_color = "green"

# Asigning points to the alien color; green, yellow, and red
if alien_color == "green":
    print("You have earned 5 points!")
elif alien_color == "yellow":
    print("You have earned 10 points!")
elif alien_color == "red":
    print("You have earned 15 points!")


# Determing the stage of life based on age
age = 23

# Telling the user what stage he/she is based on what they have put in
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is  toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is teenager.")
elif age < 65:
    print("The person is a adult.")
else:
    print("The person is an elder.")


# A list of my favorite fruits
favorite_fruits_1 = ["Banana", "Strawberry", "Blueberry", "Raspberry", 
"Mango"]

# 5 if statements to check every specific fruit is in my list, then 
# writing a statement about this kind of fruit.
if "Banana" in favorite_fruits_1:
    print("I really like Banana!")
if "Strawberry" in favorite_fruits_1:
    print("I really like Strawberry!")
if "Blueberry" in favorite_fruits_1:
    print("I really like Blueberry!")
if "Raspberry" in favorite_fruits_1:
    print("I really like Rasberry!")
if "Mango" in favorite_fruits_1:
    print("I really like mango!")

#______________________________________________________________________#
# User name data storage
user_names = []

# Checking what users are in the list and what message to send them when 
# logged in.
for user in user_names:
    if user == "admin":
        print(f"Hello {user.title()} would you like to have a status report?")
    else:
        print(f"{user.title()}, thank you for logging in again!")

# Telling program what to do if there are no users in the list
if user_names == []:
    print("We need to find some users!")


# List of current and new users
current_users = ["peter", "johan", "frank", "anja", "koen"]
new_users = ["peter", "john", "karel", "johan", "LUUK"]

# Checking if user name is available
#
# Note for my LEARNING: Something as simple as two sentences put the 
# other way around can cause a program error.
for user in new_users:
    if user in current_users:
        print(f"{user} has already been used, try another one.")
    elif user == user.upper():
        print("Upper case is not allowed!")
    elif user not in current_users:
        print(f"{user} is available!")


# List with numbers from one to 10
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Assigning st, nd, rd, and th to each number of the list
for num in number_list:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    elif num > 3 and num <= 9:
        print(str(num) + "th")