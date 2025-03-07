class Person():
    """"""
    def __init__(self, first_name, last_name, baptise_names):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.baptise_names = baptise_names.title()

    def get_full_name(self):
        """Giving full name of person."""
        print(f"{self.first_name} - {self.baptise_names} - {self.last_name}")

    def get_fn_in_dictionary(self):
        """Getting full name in dictionary."""
        full_name = {}
        full_name["First_name"] = self.first_name
        full_name["Baptise_names"] = self.baptise_names
        full_name["Last_name"] = self.last_name
        print(full_name)
