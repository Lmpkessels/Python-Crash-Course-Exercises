class Restaurant():
    """Innitialize attributes to describe a restaurant."""
    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name.title()
        self.cousine_type = cousine_type.title()

    def describe_restaurant(self):
        """Describing restaurant."""
        print(f"Restaurant_name: {self.restaurant_name}.")
        print(f"Cousien_type: {self.cousine_type}.")

    def open_restaurant(self):
        """Telling restaurant is open."""
        print(f"{self.restaurant_name} is open!")


class User():
    """Innitializing the attributes to describe user."""
    def __init__(self, first_name, last_name, user_name, email, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.user_name = user_name
        self.email = email
        self.password = password

    def describe_user(self):
        """Describing user."""
        print("\nDescribing User:")
        print(f"First_name: {self.first_name}")
        print(f"Last_name: {self.last_name}")
        print(f"User_name: {self.user_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")

    def greet_user(self):
        """Greeting user."""
        print(f"Hello, {self.first_name} {self.last_name}!")

# Creating user, assigning values to parameters.
user_koen = User(first_name="koen", last_name="kessels", user_name="koen_k94", 
                 email="koenkessels@live.nl", password="VoetbalL09!")


class IceCreamStand(Restaurant):
    """Innitializing attributes for ice cream stand."""
    def __init__(self, restaurant_name, cousine_type="Ice Cream"):
        super().__init__(restaurant_name, cousine_type)
        self.flavors = []
        
    def display_flavors(self):
        """Showing flavors in the list."""
        print(f"Here's each flavor we serve as {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

# Assigning name to parameter in IceCreamStand.
truck = IceCreamStand(restaurant_name="bassies")

# Creating list with flavors for this Ice Cream Stand.
truck.flavors = ["banana", "chocolate", "mokka", "caramel", "chocolate cookies"]

# Calling method within class to display flavors.
truck.display_flavors()


class Admin(User):
    """Initializing attributes of Admin."""
    def __init__(self, first_name, last_name, user_name, email, password):
        super().__init__(first_name, last_name, user_name, email, password)

        self.privileges = Privileges()


class Privileges():
    """Initializing attributes to Privileges."""
    def __init__(self, privileges_list=[]):
        self.privileges_list = privileges_list

    def show_privileges(self):
        """Showing privilges when assigned to user."""
        print(f"\nShowing Privileges:")
        if self.privileges_list:
            for privilege in self.privileges_list:
                print(f"- {privilege}")
        else:
            print("- No privileges are assigned.")
    
luuk = Admin("luuk", "kessels", "lmpkessels", "lmpkessels@gmail.com", 
"R-GiAe1i99!.?")

luuk_privilages = [
    "can add post",
    "can delete post",
    "can ban user",
]

luuk.privileges.privileges_list = luuk_privilages

luuk.privileges.show_privileges()


class Car():
    """Innitializing attributes to describe car."""
    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Getting a descriptive name."""
        print(f"Car_name: {self.make}") 
        print(f"Model: {self.model}")

    def read_odometer(self):
        """Reading odometer."""
        print(f"This car has {str(self.odometer_reading)} kilometers on it.")

    def update_odometer(self, kilometers):
        """Updating kilometers on odometer."""
        if kilometers >= self.odometer_reading:
            self.odometer_reading = kilometers
        else:
            print("You can't roll back the odometer.")
    
    def increment_odometer(self, kilometers):
        """Incrementing odometer."""
        self.odometer_reading += kilometers


class ElectricCar(Car):
    """Doing a simple attempt to describe a electric car."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Maybe parenteses -> (), don.t need behind Battery.
        self.battery = Battery()


class Battery():
    """Doing a simple attempt to describe a battery."""
    def __init__(self, battery_size=70):
        """Innitializing attributes for battery."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describing the battery itself."""
        print(f"This car has a {self.battery_size}-KwH engine.")

    def upgrade_battery(self):
        """Upgrading range from battery."""
        if self.battery_size < 85:
            self.battery_size = 85
        print(self.battery_size)

    def get_range(self):
        """Getting range of battery based on it's size."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = (f"This car has approximately {str(range)} range on a full" 
        " charge.")
        print(message)
    

my_car = ElectricCar(make="tesla", model="model s", year=2025)

print("\n")
my_car.battery.get_range()

my_car.battery.upgrade_battery()

my_car.battery.get_range()


