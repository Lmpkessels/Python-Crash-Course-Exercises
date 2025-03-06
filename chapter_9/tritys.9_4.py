class Restaurant():
    """Describing a restaurant or summarizing."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Describing restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Telling restaurant is open."""
        print("The restaurant is open.")

    def set_number_served(self, served):
        """Setting value to number served."""
        self.number_served = served

    def increment_number_served(self, served):
        """Incrementing number of customers served."""
        self.number_served += served

peking_garden = Restaurant("peking garden", "chinese")
peking_garden.describe_restaurant()
peking_garden.open_restaurant()

# Checking how much people restaurant has served based on default number.
print(peking_garden.number_served)

# Changing how much people restaurant has served.
peking_garden.number_served = 23
# Checking how much people restaurant has served based on modified number.
print(peking_garden.number_served)

peking_garden.set_number_served(25)
print(peking_garden.number_served)

peking_garden.increment_number_served(231)
print(peking_garden.number_served) 


class User():
    """Creating values for user profile."""
    def __init__(self, first_name, last_name, age, gender, email, user_name,
                 password):
        self.firts_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.email = email
        self.user_name = user_name
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        """Displaying user acount in dictionary."""
        user = {}
        user["first_name:"] = self.firts_name
        user["last_name:"] = self.last_name
        user["age:"] = self.age
        user["gender:"] = self.gender
        user["email:"] = self.email
        user["user_name:"] = self.user_name
        user["password:"] = self.password
        print(user)

    def increment_login_attempts(self):
        """Incrementing login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resetting login atempts."""
        self.login_attempts = 0

    def greet_user(self):
        """Greeting user."""
        print(f"Hello {self.firts_name} {self.last_name}!")

# Creating user.
luuk_kessels = User(first_name="luuk", last_name="kessels", age=25, 
                    gender="male", email="lmpkessels@gmail.com", 
                    user_name="lmp_kessels", password="RockgitAAr01908!!")

# Calling method that displays user in dictionary.
luuk_kessels.describe_user()

# Greeting user.
luuk_kessels.greet_user()

# Incrementing log in atempts.
#
# What I did wrong at first hand was, I didn't print.
print("\nIncrementing luuk's login attempts:")
luuk_kessels.increment_login_attempts()
luuk_kessels.increment_login_attempts()
luuk_kessels.increment_login_attempts()
print(luuk_kessels.login_attempts)

# Resetting login atempts.
print("\nResetting luuk's login attempts:")
luuk_kessels.reset_login_attempts()
print(luuk_kessels.login_attempts)