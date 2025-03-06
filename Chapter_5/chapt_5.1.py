# List with cars
cars = ["audi", "fiat", "mitshubishi", "bentley"]

# For loop to put out one car in upper, the rest in tile
for car in cars:
    if car == "mitshubishi": 
        print(car.upper())
    else:
        print(car.title())


# List with requested topics
requested_topping = ["Olives", "Shoarma"]

# Asking for requested toping on ordered pizza
if requested_topping != "Mushrooms":
    print("Hold the Mudhrooms!")


# Checking if two numbers are equal
answer = 22
if answer != 24:
    print("These numbers are not equal!")


# Checking if both numbers are equal to 24 by using the logical
# conditional; and
age_0 = 24
age_1 = 23
print(age_0 >= 24 and age_1 >= 24)
# Conditional (or) to see if either of the statement is true
print(age_0 >= 24 or age_1 >= 24)


# List of pizza topings
pizza_toppings = ["mushrooms", "olives", "unions", "extra cheese"]
# We use in to see if shoarma is (in) pizza toppings
print("shoarma" in pizza_toppings)

# List of banned users
banned_user = ["erik", "frans", "jakub"]
# User who's not in banned user
user = "luuk"

# Telling what to do if user is not in banned user
if user not in banned_user:
    print(user.title() + ", you can play the game!")

