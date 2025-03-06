### Excersise 6-7, People ###
# 3 Key-chains of user information
#
# User informatation of user_1
user_1 = {
    "first": "koen",
    "last": "kessels",
    "age": 23,
    "location": "stramproy",
}

# User informatation of user_2
user_2 = {
    "first": "johan",
    "last": "kessels",
    "age": 58,
    "location": "stramproy",
}

# User informatation of user_3
user_3 = {
    "first": "anja",
    "last": "kessels",
    "age": 57,
    "location": "stramproy",
}

# A list of all three users
user_list = [user_1, user_2, user_3]

# Using a for loop to print out all data we have about each user
for user in user_list:
    print(user)


### Excersise 6-7, Pets ###
# Data of pet Duck
ducky = {
    "kind": "duck",
    "owner": "dagobert",
}

# Data of pet Tom
tom = {
    "kind": "cat",
    "owner": "warner brothers",
}

# Data of pet Jerry
jerry = {
    "kind": "mouse",
    "owner": "warner brothers",
}

# Data of pet Storm
storm = {
    "kind": "dog",
    "owner": "luuk",
}

# All pets in a list
list_of_pets = [ducky, tom, jerry, storm]

# Gathering all data of each pet and showing it in the terminal
for pet in list_of_pets:
    print(pet)


### Excersise 6-9, Favorite Places: ###
# Dictionarry of poll favorite places
favorite_places = {
    "lude": "stramproy",
    "mike": "dubai",
    "koen": "singapore"
}

# Looping through the list and writing a sentence about each person his 
# favorite place in the world
for name, place in favorite_places.items():
    print(f"{name.title()} his favorite place to be is {place.title()}")


### Excersise 6-10, Favorite Numbers ###
# Poll of people their favorite number
favorite_number = {
    "anja": 30,
    "koen": 94,
    "johan": 8,
    "luuk": 29,
    "mike": 77,
}

# Getting each person his/her favorite number
for number in favorite_number.values():
    print(number)

# Nested key-chain of people who have engaged in the poll of their 
# favorite number
poll_favorite = {
    "woman": {
        "full": "anja kessels",
        "fav_1": 30,
        "fav_2": 67,
    },
    "man_1": {
        "full": "koen kessels",
        "fav_1": 94,
        "fav_2": 9,
    },
    "man_2": {
        "full": "johan kessels",
        "fav_1": 8,
        "fav_2": 67,
    },
    "man_3": {
        "full": "luuk kessels",
        "fav_1": 29,
        "fav_2": 23,
    },
    "man_4": {
        "full": "mike rietjens",
        "fav_1": 77,
        "fav_2": 68,
    }
}

"""
Fix error and make sure every name is printed out, think about it don't
rush the process, understanding is way more important!

Good Luck! :)
"""

# Telling what their favorite numbers are
for gender, favorite in poll_favorite.items():
    if "woman" in gender:
        print(f"{favorite["full"].title()} her favorite numbers are "
        f"{favorite["fav_1"]}, and {favorite["fav_2"]}")
    elif "man" in gender:
        print(f"{favorite["full"].title()} his favorite numbers are "
        f"{favorite["fav_1"]}, and {favorite["fav_2"]}")


### Excersise 6-11, Cities ###
# Dictionary called cities
cities = {
    "bangkok": { 
    "country": "thailand",
    "population": 11000000, 
    "fact": "Bangkok's full ceremonial name is 168 letters long, making"
    " it the longest city name in the world.",
    },

    "dubai": {
    "country": "united arab emirates",
    "population": 3300000, 
    "fact": "Dubai is home to the world's tallest building, the Burj" 
    " Khalifa, standing at 828 meters.",
    },

    "monaco": {
    "country": "monaco (a sovereign city-state)",
    "population": 39000, 
    "fact": "Monaco is the second smallest independent state in" 
    "the world, covering just over 2 square kilometers."
    },
}

# Looping through cities and telling where it is based (country), 
# how big its population is, and a fact about the city
#
# Using an if...elif...else.... chain to be specific about each city
for name, data in cities.items():
    print(f"\n{name.title()}")
    if name == "bangkok":
        print(f"Bangkok is a place in {data["country"].title()} it has" 
              f" a population of {data["population"]} and here's a fact" 
              f" about Bangkok {data["fact"]}")
    elif name == "dubai":
        print(f"Dubai is a place in {data["country"].title()} it has" 
              f" a population of {data["population"]} and here's a fact" 
              f" about Dubai {data["fact"]}")
    elif name == "monaco":
        print(f"{data["country"].title()} has a population of" 
              f"{data["population"]} and here's a fact about Monaco," 
              f"{data["fact"]}")
        
