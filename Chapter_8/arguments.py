### Positiona Arguments ###
# Describing what kind of pet I have.
def describe_pet(animal_type, pet_name):
    """Describing information about a pet"""
    print(f"I have a {animal_type} called {pet_name.title()}.")

# Declaring what kind of pet it is and it's name.
describe_pet("duck", "franky")

# Describing what kind of pet and what his/her name is.
def describe_pet(animal_type, pet_name):
    """Describing information about a pet"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Declaring what kind of pet it is and it's name.
describe_pet("snake", "john")

### Multiple Function Calls ###
# Here we recal the function only with different values to show that,
# you can call a function as many times as you want.
describe_pet("lion", "bear")
describe_pet("monkey", "jacky")
describe_pet("goldfish", "asset")

### Order Matters in Positional Arguments ###
# Here we show that order matters, because if you twist things around,
# things can start to look very weard.
#
# Wrong version
describe_pet("john", "bear")

# Right version
describe_pet("bear", "john")


### Keyword Arguments ###
# By using keyword arguments (e.g. pet_name=) you can't make order 
# mistakes.
describe_pet(pet_name="frank", animal_type="rat")
describe_pet(animal_type="fish", pet_name="luuk")


### Default Values ###
# Describing a person with it's default value set to man.
def describe_person(name, gender="man"):
    """Describing what name and gender person is."""
    print(f"{name.title()} is a {gender}")

# Here I declare a name to the person, in the second sentence I change 
# the default value.
describe_person("luuk")

# Here the default value gets ignored.
describe_person("anja", gender="woman")

# This will cause a error, because some values are missing.
describe_person()