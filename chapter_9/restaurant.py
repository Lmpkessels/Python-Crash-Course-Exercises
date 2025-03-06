class Restaurant():
    """Innitializing attributes for a restaurant."""
    def __init__(self, name, location, adress, kitchen):
        self.name = name.title()
        self.location = location.title()
        self.adress = adress
        self.kitchen = kitchen.title()
        self.number_served = 0

    def get_descriptive_restaurant(self):
        """
        Getting descriptive name of restaurant.
        And describing what food they serve.
        """
        description = {}
        description["Restaurant_name"] = self.name
        description["Location"] = self.location
        description["Adress"] = self.adress
        description["Kitchen"] = self.kitchen
        print(description)

    def open_restaurant(self):
        """Telling that the restaurant is open."""
        print("How you should write the time: 17.00, use a dot (.) in" 
              " between.")
        time = float(input("Tell me the time in 24-hour-clock: "))
        if time < 16.00 and time > 21.00:
            print("Closed.")
        else:
            print("Open.")

    def number_served(self, number):
        """Seeing how many people are served."""
        self.number_served = number

    def increment_number_served(self, number):
        """Incrementing the number of people served."""
        self.number_served += number

    