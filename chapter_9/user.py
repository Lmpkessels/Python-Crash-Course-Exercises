"""Doing a simple attempt to create certain aspects of a user profile."""
import user_admin

class User():
    """Creating a user profile."""
    def __init__(self, first_name, last_name, user_name, user_email, password):
        """Innitializing attributes for User."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.user_name = user_name
        self.user_email = user_email
        self.password = password
        self.login_attempts = 0
        self.privileges = user_admin.Privileges()

    def get_user_description(self):
        """Describing user in dictionarry."""
        user = {}
        user["First_name"] = self.first_name
        user["Last_name"] = self.last_name
        user["User_name"] = self.user_name
        user["User_email"] = self.user_email
        user["Password"] = self.password
        print(user)

    def greet_user(self):
        """Greeting user."""
        print(f"Hello, {self.first_name} {self.last_name}!")
        
    def increment_attempts(self):
        """Incrementing login attempts by one."""
        self.login_attempts += 1

    def reset_attempts(self):
        """Resetting login attempts to zero."""
        self.login_attempts = 0
