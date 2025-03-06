### Excersise 8-3, T-shirt ###
def make_shirt(size, print_on_shirt):
    """Summarizing size of t-shirt and text print on shirt."""
    summary = f"Size: {size} \nText print: {print_on_shirt}"
    print(f"\n{summary.title()}")

# Creating shirt and then calling the function.
make_shirt("large", "luuk is awesome")
make_shirt(size="large", print_on_shirt="luuk is awesome",)


### Excersise 8-4, Large Shirts ###
def make_shirt(size="large", text="python is awesome"):
    """Summarizing default t-shirt."""
    shirt = f"\nSize: {size.title()} \nText print: {text.title()}"
    print(shirt)

# Calling default function, and modified function.
make_shirt()
make_shirt(size="medium")


### Excersise 8-5, Cities ###
def describe_city(city_name, country_located):
    """Summarizing a city name and where it is located."""
    msg = f"\n{city_name.title()} is in {country_located.title()}."
    print(msg)

# Calling function where I have assigned, values to the parameters.
describe_city("utrecht", "the netherlands")
describe_city(city_name="monaco", country_located="monaco")

