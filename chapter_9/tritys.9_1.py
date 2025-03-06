class Restaurant():
    """Summarizing everything about restaurant."""
    def __init__(self, restaurant_name, cuirsine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuirsine_type = cuirsine_type.title()

    def describe_restaurant(self):
        """Describing restaurant."""
        print(f"{self.restaurant_name} has a {self.cuirsine_type} " 
              "kitchen.")

    def open_restaurant(self):
        """Telling user if restaurant is open."""
        print("Restaurant is open!")

print("\n")
# Describing three restaurants.
#
# Asigning name of restaurant and kind of food they serve.
paking_garden = Restaurant("paking garden", "chinese")
# Describing restaurant.
paking_garden.describe_restaurant()
# Checking if restaurant is open.
paking_garden.open_restaurant()

print("\n")
# Asigning name of restaurant and kind of food they serve.
rodeo_eindhoven = Restaurant("rodeo eindhoven", "amerikan/mexican")
# Describing restaurant.
rodeo_eindhoven.describe_restaurant()
# Checking if restaurant is open.
rodeo_eindhoven.open_restaurant()

print("\n")
# Asigning name of restaurant and kind of food they serve.
hof_van_keent = Restaurant("hof van keent", "dutch")
# Describing restaurant.
hof_van_keent.describe_restaurant()
# Checking if restaurant is open.
hof_van_keent.open_restaurant()


class User():
    """About user."""
    def __init__(self, first_name, last_name, age, gender, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender.title()
        self.email = email

    def describe_user(self):
        """Summarizing user."""
        print(f"name: {self.first_name}, last_name: {self.last_name}, "
              f"age: {self.age}, gender: {self.gender}, email: {self.email}")
        
    def great_user(self):
        """Greeting user."""
        print(f"Hello, {self.first_name} {self.last_name}!")

# Creating for users.
#
# Creating user.
print("\n")
user_anja = User(first_name="anja", last_name="kessels", age=57, gender="woman", 
                 email="anjakessels@live.nl")
# Describing user.
user_anja.describe_user()
# Greeting user.
user_anja.great_user()

# Creating user.
print("\n")
user_johan = User(first_name="johan", last_name="kessels", age=58, gender="man", 
                 email="johankessels@live.nl")
# Describing user.
user_johan.describe_user()
# Greeting user.
user_johan.great_user()

# Creating user.
print("\n")
user_koen = User(first_name="koen", last_name="kessels", age=23, gender="man", 
                 email="koenkessels@live.nl")
# Describing user.
user_koen.describe_user()
# Greeting user.
user_koen.great_user()

# Creating user.
print("\n")
user_luuk = User(first_name="luuk", last_name="kessels", age=25, gender="man", 
                 email="luukkessels@live.nl")
# Describing user.
user_luuk.describe_user()
# Greeting user.
user_luuk.great_user()