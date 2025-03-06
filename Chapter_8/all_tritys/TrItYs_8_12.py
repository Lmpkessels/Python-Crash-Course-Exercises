### Excersises 8-12, Sandwiches ###
# Function that accepts a list of items a person wants on a sandwich.

def sandwhiches(*items):
    """Summarizing sandwhich"""
    print("\nHere follows a ingredients list for ordered sandwich:")
    for item in items:
        print(f"- {item.title()}")

# Creating sandwhich
sandwhiches("bacon", "chicken", "cheese", "rucola",)


### Excersise 8-13, User-profile ###
# Defining a function called user profile.
def build_profile(first_name, last_name, **about):
    """Profile of user, getting name, last name, and about."""
    # Creating dictionary
    profile = {}
    profile["first_name:"] = first_name
    profile["last_name:"] = last_name

    # Creating key-value pair for about, so we can create based on our thoughts
    # not set in stone values.
    for key, value in about.items():
        profile[key] = value
    return profile

# Calling user profile and asigning values to parameters.
profile = build_profile(first_name="luuk", last_name="kessels", age=25, 
              sport="Weight-training and Kickboxing")

# Displaying user profile.
print(f"\n{profile}")


### Excersise 8-14, Cars ###
# Defining a function called about_car, with two needed parameters 
# (manufacturer, and model_name) and one optional.
def about_car(manufacturer, model_name, **more):
    about = {}
    about["Manufacturer:"] = manufacturer.title()
    about["Model_name:"] = model_name.title()

    # Getting key and value in more so we can create our own key value pairs.
    for key, value in more.items():
        about[key] = value
    return about

# Creating about, assigning values to parameters.
about = about_car(manufacturer="rolls royce", model_name="phantom", year=2025, 
          engine="v8")

# Displaying about.
print(about)