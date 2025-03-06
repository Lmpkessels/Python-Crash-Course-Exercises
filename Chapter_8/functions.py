# Greeting a user we use def to define a function, the function is 
# greet_user().
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()


# Greeting user by user_name
def greet_user(user_name):
    """Greeting user by name."""
    print(f"Hello, {user_name.title()}!")

# Here we greet user by name, how - simply by putting "luuk" in between 
# ("quotations").
#
# You can use this function as many times as you want.
greet_user("luuk")