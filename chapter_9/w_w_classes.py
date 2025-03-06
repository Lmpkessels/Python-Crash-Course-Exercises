class Car():
    """A simple attempt to represent a car."""
    # __init__ is called a method.
    def __init__(self, make, year, model):
        self.make = make
        self.year = year
        self.model = model
        self.odometer_reading = 0
    
    def update_odometer(self, mileage):
        """Updating odometer."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer.")
    
    def increment_odometer(self, increment):
        """Adding miles to odometer."""
        self.odometer_reading += increment

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        descriptive_name = (f"make: {self.make} - year: {self.year} - " 
        f" model: {self.model}")
        return descriptive_name
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {str(self.odometer_reading)} miles on in.")

# Creating car description. Assigning values to, parameter.
my_new_car = Car(make="ferrari", year=2024, model="f818")
# Displaying function.
print(my_new_car.get_descriptive_name())
# Asigning new value to odometer reading.
my_new_car.update_odometer(23)
# Calling read odometer.
my_new_car.read_odometer()
# Incremening odometer.
my_new_car.increment_odometer(23321)
# Reading odometer.
my_new_car.read_odometer()

