# We add this module-level docstring to briefly describe this document.
"""A class that can be used to represent a car."""

class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model
        self.year = year
        self.odometer_count = 0

    def get_descriptive_name(self):
        """Getting a descriptive name."""
        car = {}
        car["Make:"] = self.make
        car["Model:"] = self.model
        car["Year:"] = self.year
        car["Odometer_count:"] = self.odometer_count
        print(car)

    def read_odometer(self):
        """Reading odomoter."""
        print(f"This car has {self.odometer_count} kilometers on it.")

    def update_odometer(self, kilometers):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if kilometers >= self.odometer_count:
            self.odometer_count += kilometers
            print(self.odometer_count)
        else:
            print("You can't roll back the odometer.")

    def increment_odometer(self, kilometers):
        """Incrementing odometer count."""
        self.odometer_count += kilometers