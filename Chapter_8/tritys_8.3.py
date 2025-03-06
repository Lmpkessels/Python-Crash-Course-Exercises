### Excersise 8-3, T-shirt ###
# Here we use positional arguments to declare what the t-shirt will 
# become.
def make_shirt(size, text):
    """Sumarizing size and text on t-shirt."""
    print(f"Size of t-shirt is {size} and the text on t-shirt is",
           f" {text}")

# Here we make the t-shirt. (these are positional arguments.)
make_shirt("M", "Luuk is awesome!")

# Here you see why we don't choose them.
#
# The reason is because it the function doesn't care in what order the
# values given come.
make_shirt("Luuk is awesom", "Medium")

# Here we use keyword arguments.
def make_shirt(size, text):
    "Summarizing size and text on t-shirt."
    print(f"The size of t-shirt is {size} and the text will be {text}.")

# Creating t-shirt. (what you see here are keyword arguments.)
make_shirt(size="Medium", text="We are champions!")


### Excersise 8-4, Large Shirt ###
# Here we define a defauls size for the function and a default text.
#
# Then we summarize the t-shirt and text.
def make_shirt(size="large", text="I love Python"):
    """Summarizing size and text of t-shirt."""
    print(f"Size of t-shirt is {size.title()} and text on it is {text}.")

# Here we create the default one, and the other one we change it's size.
make_shirt()
make_shirt(size="Medium")


### Excersise 8-5, Cities ###
# Describing something about a village and in what country it is.
def describe_city(city, country):
    """A simple descripion about city and location of it."""
    print(f"{city.title()} is a village in the {country.title()}.")

# Here we define about what city we talk and in what country it is.
describe_city(city="stramproy", country=("netherlands"))

