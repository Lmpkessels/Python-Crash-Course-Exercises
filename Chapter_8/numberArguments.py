### Passing an Arbitrary number of Arguments ###

# The (*) makeses sure you can modify the list as you like.
#
# The (*) is called asterisk and tells python to make an empty tuple.
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

# The requested toppings.
make_pizza("mushrooms", "extra cheese", "olives")


### Mixing Positional and Arbitrary Arguments ###
def build_profile(first, last, middle="", **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    profile["middle_name"] = middle
    
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Creating dictionary based on our input.
user_profile = build_profile(first="albert", last="einstein", 
location="princetion", field="physics")

# Displaying user profile.
print("\n", user_profile)