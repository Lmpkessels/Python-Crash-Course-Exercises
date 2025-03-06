class Car():
    """Initializing specific car details."""
    def __init__(self, car_name, model, engine, year_build):
        self.car_name = car_name
        self.model = model
        self.engine = engine
        self.year_build = year_build
        self.odometer_stand = 0
        self.fill_gas_tank = 0

    def description_list(self):
        """Description list of car."""
        print(f"Car_name: {self.car_name}")
        print(f"Model: {self.model}")
        print(f"Engine: {self.engine}")
        print(f"Year_build: {self.year_build}")
        print(f"Odometer_stand: {self.odometer_stand}")

    def about_enginge(self, celinders, power, transmission, zero_hundred, 
                      top_speed):
        """Description about engine."""
        engine = {}
        engine["Celinders:"] = celinders
        engine["Power:"] = power
        engine["Transmission:"] = transmission
        engine["zero_to_hundred:"] = zero_hundred
        engine["Top_speed:"] = top_speed
        print(engine)

    def gas_tank(self, liters):
        """Defining liters in gass tank."""
        self.fill_gas_tank += liters

    def descriptive_sentence(self):
        """Giving a descripive sentence."""
        print(f"{self.car_name} - {self.model} - {self.engine}")

    
    def update_odometer(self, mileage):
        """Checking odometer stand."""
        if mileage >= self.odometer_stand:
            self.odometer_stand = mileage
        else:
            print("You can't roll back the odometer.")

    def increment_odometer(self, miles):
        """Incrementing odometer."""
        self.odometer_stand += miles

# Describing my car asigning and asigning values to the attributes.
my_car = Car(car_name="rolls royce", model="phantom", engine="v8", 
             year_build=2025,)

# Incrementing odometer to new milage.
my_car.increment_odometer(2300)

my_car.gas_tank(50)


class Engine():
    """Declaring default engine."""
    # default_engine should have a value asigned to it, otherwise you get an 
    # error.
    def __init__(self, engine_size, default_engine="v12"):
        self.engine_size = engine_size
        self.default_engine = default_engine

    def describe_engine(self):
        """Describing default engine."""
        print(f"This car has a {self.default_engine}.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.engine_size == 819:
            range = 9000
        elif self.battery_size == 948:
            range = 9444
        
        message = f"This car can go approximately {str(range)}"
        message += " miles on full power."
        print(message)


class SportsCar(Car):
    """Describing my new sports car."""
    def __init__(self, car_name, model, engine, year_build):
        super().__init__(car_name, model, engine, year_build)
        # Using another class in this class to keep the code clean.
        #
        # You can change the engine within here so you can set it specific to 
        # the car your describing.
        self.default = Engine(819)

    def makes_unique(self):
        """Describing what makes this car unique."""
        print(f"The {self.car_name} {self.model} has a 4 wheel steering, " 
              "is a light weight sports car and it's original color is red.")

# Creating car.
ferrari_818 = SportsCar(car_name="ferrari", model=818, engine="v12", 
                        year_build=2025)

# Creating dictionary about the ferrari 818 motor.
print("\n")
ferrari_818.about_enginge(celinders="v12", power="830 Hp", 
                          transmission="8-speed dual-clutch automatic", 
                          zero_hundred=2.9, top_speed="340km/h")

# Showing description list about car.
print("\n")
ferrari_818.description_list()

# Calling what makes the car unique.
print("\n")
ferrari_818.makes_unique()

# Calling method to describe default engine.
ferrari_818.default.describe_engine()
ferrari_818.default.get_range()


class ElectricCar(Car):
    """Describing a electric car."""
    def __init__(self, car_name, model, engine, year_build):
        super().__init__(car_name, model, engine, year_build)

    # Here I override the method in the parents class.
    def gas_tank(self):
        """Telling it has not gas tank."""
        print("This car doesn't have a gas tank.")

# Creating car description.
tesla = ElectricCar(car_name="tesla", model="s", engine="12v", 
                    year_build="2021")

# Here I call the method.
tesla.gas_tank()


