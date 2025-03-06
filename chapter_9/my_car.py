from car import Car
from electric_car import ElectricCar

my_sports_car = Car(make="ferrari", model=818, year=2024)
my_electric_car = ElectricCar(make="tesla", model="s", year=2021)

my_sports_car.update_odometer(1223)
my_sports_car.get_descriptive_name()

my_electric_car.get_descriptive_name()
my_electric_car.battery.get_range()