def build_profile(first_name, last_name, **about):
    """Creating customer profile."""
    profile = {}
    profile["first_name:"] = first_name.title()
    profile["last_name:"] = last_name.title()

    # Getting key-value-chain in about.
    for key, value in about.items():
        profile[key] = value
    return profile

# Creating profile, asigning values to parameter.
profile = build_profile(first_name="luuk", last_name="kessels", age=25, 
              birthday="23-02-2000")

# Displaying profile.
print(profile)


def about_car(manufacturer, model_name, **about):
    """Describing information about a car."""
    information = {}
    information["manufacturer:"] = manufacturer.title()
    information["model_name:"] = model_name.title()

    # Creating a key-value chain for about, so we can choose ourselfs what 
    # information we give, this is optional.
    for k, v in about.items():
        information[k] = v
    return information

# Creating description about the car.
car = about_car(manufacturer="solihull plant", 
                model_name="land rover - defender", year=2025, 
                engine="v8")

# Displaying the description.
print(car)