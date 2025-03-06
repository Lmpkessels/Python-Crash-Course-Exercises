class Car():
    """A simple attempt to represent a car."""
    def __init__(self, car_name, model, year, engine):
        self.car_name = car_name
        self.model = model
        self.year = year
        self.engine = engine
        self.odometer_reading = 0

    def get_descriptive_list(self):
        """Getting a descriptive list."""
        print(f"\nName: {self.car_name}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Enginge: {self.engine}")
        print(f"Odometer_reading: {self.odometer_reading}")

    def get_descriptive_name(self):
        """Getting descriptive name."""
        long_name = (f"car name: {self.car_name}, model: {self.model}," 
                     f" engine: {self.engine}")
        return long_name.title()
    
    def update_odometer(self, mileage):
        """Updating maliage odometer."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer.")

    def increment_odometer(self, miles):
        """Incrementing odometer."""
        self.odometer_reading += miles

# Creating car.
car = Car(car_name="audi", model="rs6", year=2025, engine="v8")

car.increment_odometer(2333)

# Getting descriptive list of car.
car.get_descriptive_list()

print("\n")
# Getting descriptive name of car.
print(car.get_descriptive_name())

# ElectricalCar is the child class, and within the parenteces is the parent 
# class -> Car.
print("\n")
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, car_name, model, year, engine):
        super().__init__(car_name, model, year, engine)

# Here we create the ElectricCar.
my_car = ElectricCar("tesla", "s", "2025", "3-phase alternating current" 
                     " induction motors")

# Here we get the descriptive name of the car, won out of parent class Car.
print(my_car.get_descriptive_name())


print("\n")
# RaceCar is the name to describe the child class within the parentheses of the
# child class is the parent.
class RaceCar(Car):
    """Representing a f1 racecar."""
    def __init__(self, car_name, model, year, engine):
        super().__init__(car_name, model, year, engine)

# Here we create the care and give the parameters values.
red_bull_f1_car = RaceCar(car_name="RB21", model="RB21", year="2025", 
                          engine="Honda RBPTH002")

# Here we get the descriptive list within the parent class Car.
red_bull_f1_car.get_descriptive_list()

# Here we print a descriptive name, also gotten out of the parent class.
print(red_bull_f1_car.get_descriptive_name())


print("\n")
# OldTimer is the child class, and within the parenteces is the parent class car.
class OldTimer(Car):
    """Represent aspects of a car, specific to old-timer vehicles."""
    def __init__(self, car_name, model, year, engine):
        super().__init__(car_name, model, year, engine)
    
# Creating a old timer car. Assigning values to the atributes.
ford_mustang = OldTimer(car_name="ford mustang", model="1967 Shelby GT500",
                        year=1967, engine="7.0L V8 (428 Cubic inch Cobra Jet)")

# Getting descriptive name of the ford mustang.
print(ford_mustang.get_descriptive_name())

# Incrementing milage on odometer.
ford_mustang.increment_odometer(22388)

# Getting descriptive list of the ford mustang.
ford_mustang.get_descriptive_list()