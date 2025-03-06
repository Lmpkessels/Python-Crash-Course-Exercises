### Excersise 8-12, Sandwiches ###
def sandwich_items(*items):
    """Summarizing ordered sandwich."""
    for item in items:
        print(f"- {item.title()}")

# Showing summary of collected items.
print("Here is a summary of the collected items:")

# List of ordered sandwich items.
sandwich_items("chicken", "bacon", "salad", "unions",)


### Excersise 8-13, User Profile ###
# Building a user profile.
def build_profile(first_name, last_name, **about):
    """Creating a user profile."""
    person = {}
    person["first_name:"] = first_name.title()
    person["last_name:"] = last_name.title()

    # Getting key and value of pair in about.
    for key, value in about.items():
        person[key] = value
    return person

# Creating person. 
profile = build_profile(first_name="luuk", last_name="kessels", age="25", 
                        gender="male", 
                        sports="weightlifting and kickboxing")

# Showing person.
print("\n", profile)


### Excersise 8-14, Cars ###
# Storing information about a car.
def store_car_information(manufacturer, model, **items):
    """Storing information about a car."""
    # Creating an empty dictionary to store data.
    about = {}
    about["manufacturer:"] = manufacturer
    about["model:"] = model

    # Getting key, value in items.
    for key, value in items.items():
        about[key] = value
    return about

# Creating a variable to assign values to function.
car = store_car_information(manufacturer="audi", model="rs3", 
                            year="2025", color="grey", engine="v8")

# Showing car.
print("\n", car)