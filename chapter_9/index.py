class Restaurant():
    """Giving information about a restaurant."""
    def __init__(self, restaurant_name, location, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.location = location.title()

    def describe_restaurant(self):
        """Describing restaurant."""
        print(f"{self.restaurant_name} located in {self.location} serves " 
              f"{self.cuisine_type}.")

    def open_restaurant(self):
        """Telling restaurant is open."""
        print("The restaurant is open!")


print("\n")
# Asigning values to parameters in __init__ to create restaurant.    
restaurant = Restaurant("paking garden", "stramproy", "chinese")
# Calling function within class that describes restaurant.
restaurant.describe_restaurant()
# Checking if restaurant is open.
restaurant.open_restaurant()


print("\n")
# Creating restaurant by asigning values to parameters in __init__.
restaurant_0 = Restaurant("rodeo", "eindhoven", "amerikan/mexican")
# Calling function within class that describes restaurant.
restaurant_0.describe_restaurant()
# Checking if restaurant is open.
restaurant_0.open_restaurant()


print("\n")
# Creating restaurant by asigning values to parameters in __init__.
restaurant_1 = Restaurant("hof van keent", "weert", "dutch")
# Calling function within class that describes restaurant.
restaurant_1.describe_restaurant()
# Checking if restaurant is open.
restaurant_1.open_restaurant()


class User():
    """Storing a user profile."""
    def __init__(self, name, last_name, age, email):
        self.name = name.title()
        self.last_name = last_name.title()
        self.age = age
        self.email = email

    def describe_user(self):
        """Summarizing user profile."""
        summary = {}
        summary["first_name:"] = self.name
        summary["last_name:"] = self.last_name
        summary["age:"] = self.age
        summary["email:"] = self.email
        print(summary)
    
    def greet_user(self):
        """Personalized greeting for user."""
        print(f"Hello, {self.name} {self.last_name}!")

# Creating user.
user_koen = User(name="koen", last_name="kessels", age=23, 
                 email="koenkessels@live.nl")

print("\n")
# Calling function within class, to show person summarized in dictionary.
user_koen.describe_user()

# Greeting user.
user_koen.greet_user()

