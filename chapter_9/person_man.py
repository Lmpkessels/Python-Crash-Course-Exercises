"""This module is set in stone to man."""
# Importing person class - a.k.a parents class.
import person

class PersonMan(person.Person):
    """Innitializing gender attribute for person man."""
    def __init__(self, first_name, last_name, baptise_names, gender="man"):
        super().__init__(first_name, last_name, baptise_names)
        self.gender = gender
        # Testing how I can get methods from parent class into childs class.
        self.get_full_name
        self.get_fn_in_dictionary
    
    def person_gender(self):
        """Describing gender."""
        print(f"This is a {self.gender}")