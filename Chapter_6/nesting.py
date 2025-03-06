# Storing customer in key-chain
customer_1 = {"name": "luuk", "lastname": "kessels"}
customer_2 = {"name": "jan", "lastname": "mans"}
customer_3 = {"name": "peter", "lastname": "franken"}

# Asigning all customers to a List
customers = [customer_1, customer_2, customer_3]

# Looping through the list and putting out each customer in the terminal
for customer in customers:
    print(customer)


# An empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Changing statistics of 5 aliens
for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "Yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = "15"

# Showing the first 5 aliens
#
# This [0:1] is called a slice, and is used to get a specific amount of 
# items out of a list
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)), "\n")

### A list in a dictionary ###
# Store information about a pizza being ordered
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
    }

# Summarize the order
print("You ordered a " + pizza["crust"] + "-crust pizza " + 
    "with the following toppings")

# Telling employe what toppings to add on the pizza
for topping in pizza["toppings"]:
    print("\t" + topping)

# Key chain with a list of favorite languages added to it
favorite_languages = {
    "luuk": ["python", "javascript"],
    "jan": ["html", "css"],
    "johan": ["c"],
    "anja": ["c++", "python"]
    }

# Telling what each ones favorite languages are based on poll
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


### A Dictionary in a Dictionary ###
# Key chains about the user their information
users = {
    "lmpkessels": {
        "first": "luuk",
        "last": "kessels",
        "location": "stramproy",
    },
    "amgkessels": {
        "first": "anja",
        "last": "kessels",
        "location": "stramproy",
    }
}

# Using a for loop to loop through the nested key-chain, getting in and
# putting out full names and location of the user
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]

# Telling the full name of the user and its location
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

