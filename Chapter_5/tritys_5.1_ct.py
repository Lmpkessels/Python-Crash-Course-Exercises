### Excersise 5-1. Conditional Test ###

# Creating statement
car = "audi"

# Predicts statement is True
print(car == "audi", "I predict this statement is True!")

# Predicts statement is False
print(car == "toyota", "I predict this statement is False!")


# 10 test to see if statement is True or False
#
# Telling who my brother is
brother = "koen"
print(brother == "koen", "I predict this statement is True!")
print(brother == "Koen", "I predict this statement is False!")
print(brother.title() == "Koen", "I predict this statement is True!")


# Declaring if my name is Luuk
my_name = "luuk"
print(my_name == "jan", "I predict this statement is False!")
print(my_name.upper() == "LUUK", "I predict this statement is True!")


# Checking if the weather is sunny outside
weather = "sunny"
print(weather == "sunny", "I predict this statement is True!")
print(weather == "rainy", "I predict this statement is False!")
print(weather.title() == "rainy", "I predict this statement is False!")


# Seeing if my age is 24
my_age = 24
print(my_age == 24, "I predict this statement to be True!")
print(my_age == 28, "I predict this statement to be False!")


### Excersis 5-2. More Conditional Tests ###

# Assigning toppics to variable
topping = "kebab"
topping_1 = "champignons"

# Using logical operater (and) to see if statements are True
# both need to be True for whole statement to be True.
print(topping == "kebab" and topping_1 == "champignons")
print(topping == "Meatloaf" and topping_1 == "champignons")


# Using logical operater (or) to see if statement is True,
# one of two need to be True for whole statement to be True.
print(topping == "Meatloaf" or topping_1 == "champignons")

# Testing if test is True or False using operators .lower, .upper,
# and .title .
test = "lower"
print(test.lower() == "lower", "This statement is True!")
print(test.upper() == "lower", "This statement is False!")
print(test.title() == "Lower", "This statement is True!")


# Declaring a variable called number
number = 26

# Cheking if number is greater then or equal to
print(number >= 26)

# Checking if number is less then or equal to
print(number <= 26)


# Declaring a variable called number
number = 25 

# Checking if number is equal to or greater then 25 and equal to or less
# then 30.
#
# Using logical AND operator
print(number >= 25 and number <= 30, "I predict this statement to be True!")

# Checking if number is greater then or equal to 25 and greater then or
# equal to 30.
#
## Using logical AND operator
print(number >= 25 and number >= 30, "I predict this statement to be False!")

# Checking if number is greater then or equal to 25 or if number is 
# less then or equal to 30.
#
# Using logical OR operator
print(number >= 25 or number <= 30, "I predict this statement to br True!")

# Checking if number is greater then or equal to 25 or if number is 
# greater then or equal to 30.
#
# Using logical OR operator
print(number >= 25 or number >= 30, "I predict this statement to be True!")


# Different kinds of transport
transport_list = ["car", "truck", "heftruck", "bus"]

# Checking if bike is in transport list
#
# Using logical IN operator
print("bike" in transport_list, "I predict this statement is False!")

# Checking if car is not in transport list
#
# Using logical NOT and IN operator
print("car" not in transport_list, "I predict this statement is False!")