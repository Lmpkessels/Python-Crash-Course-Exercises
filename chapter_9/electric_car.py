from car import Car

class Battery():
    """A simple attempt to describe a electric car battery."""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """Describing battery."""
        print(f"This car has {self.battery_size}-KwH battery engine.")

    def get_range(self):
        """Get battery range."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        # Telling the user the range on full charge based on battery size.
        message = f"This battery has a range of {str(range)} on full charge."
        print(message)


class ElectricCar(Car):
    """Doing a simple atempt do describe a electric car."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()