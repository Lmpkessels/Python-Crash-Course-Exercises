class Restaurant():
    """Describing a restaurant or summarizing."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.time = 0

    def describe_restaurant(self):
        """Describing restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Telling restaurant is open."""
        if self.time >= 1700 and self.time <= 2300:
            print("The restaurant is open.")
        else:
            print("Sorry, were closed.")


peking_garden = Restaurant("peking garden", "chinese")
peking_garden.describe_restaurant()
peking_garden.describe_restaurant(1700)