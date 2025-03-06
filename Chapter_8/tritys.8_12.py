### Excersise 8-12, Sandwiches ###
# Function with a list of items a person wants on his sandwich.
def items_sandwich(*items):
    """Creating a list of items the person wants on its sandwhich."""
    for item in items:
        print(f"- {item.title()}")

# Showing list of requested toppings.
print("Here follows the ingredient list for sandwich:\n")

# Calling function with requested toppings
items_sandwich("chicken", "bacon", "pine nuts", "unions", "salad",)


### Excersise 8-13, User Profile ###
# Defining a function for user profile.
def user_profile(first_name, last_name, **about):
    """
    Defining a user profile.
    It describes; first, last, and about.
    """
    profile = {}
    profile["first_name"] = first_name.title()
    profile["last_name"] = last_name.title()

    # Getting key and value of key value chain. Then we return profile.
    #
    # We use the dictionary method .items() to access the dictionary.
    for key, value in about.items():
        profile[key] = value
    return profile

# Here we create the person with our give values.
person = user_profile(first_name="luuk", last_name="kessels", 
             baptismal_names="martinus petrus", 
             sport="kickboxing and weightlifting",
             working_on="programming")

# Displaying person in terminal.
print("\n", person)


### Excerise 8-14, Cars ###
# A function that stores information about a car.
def car_information(manufacturer, model, **arguments):
    """Making a summary of the given information."""
    information = {}
    information["Manufacturer:"] = manufacturer
    information["Model"] = model

    # Getting key and value in arguments, because its a dictionary, 
    # so it's a key-value pair.
    #
    # Don't forget items(), without items you don't get access to the 
    # dictionary.
    #
    # Return needs to be outside of the loop because if return is early 
    # then the loop exits early because it wants to return.
    for key, value in arguments.items():
        # Here we look up the key in the dictionary.
        information[key] = value
    return information

# Creating values of car information and asign it to the dictionary.
car = car_information(manufacturer="audi", model="rsq8", color="Blue", 
                      engine="v12", straightpiped="True")

# Displaying created car dictionary.
print(car)


# Create a function about user information.
#
# We use ** or * to create our own values, so now we have 2 first and 
# last that must be generated, and about is optional.
def user_information(first_name, last_name, **about):
    """Summarizing information about given person."""
    information = {}
    information["first_name:"] = first_name.title()
    information["last_name:"] = last_name.title()

    # Get key and value.
    for key, value in about.items():
        information[key] = value
    return information

# Create values of car information and asign it to dictionary.
person = user_information(first_name="luuk", last_name="kessels", 
                          gender="male", age="25")

# Display created car dictionary.
print("\n", person)


# Create a function about city.
def information_city(city_name, country, **about):
    """Summarizing city, giving name, country, and fact."""
    information = {}
    information["city_name:"] = city_name.title()
    information["country:"] = country.title()

    # Get key-value.
    for key, value in about.items():
        information[key] = value
    return information

# Create values of city information and asign it to dictionary.
city_information = information_city(city_name="monaco", country="monaco", 
                                    population="39,050", 
                                    government="House of Grimaldi")

# Display created car dictionary.
print("\nHere you see the city summary:")
print(city_information)

name = input("\nWhat is your name? ")
print(f"\nGreat job today {name.title()}!")

