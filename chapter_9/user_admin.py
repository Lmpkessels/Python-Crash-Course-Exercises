import user
class Privileges():
    """Creating a class for privileges of specific users."""
    def __init__(self, privileges_list=[]):
        self.privileges_list = privileges_list
    
    def show_privileges(self):
        """Showing assigned privileges to user."""
        print("Showing privileges:")
        if self.privileges_list:
            for privilege in self.privileges_list:
                print(f"- {privilege}")
        else:
            print("- This user has no assigned privileges to it's account.")


class Admin(user.User):
    """Innitializing attributes for Admin."""
    def __init__(self, first_name, last_name, user_name, user_email, password):
        super().__init__(first_name, last_name, user_name, user_email, password)
        self.privileges = Privileges()
