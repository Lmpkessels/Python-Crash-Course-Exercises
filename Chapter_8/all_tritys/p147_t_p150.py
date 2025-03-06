# Defining a function, to greet users.
#
# Using a for loop to get each name out of the parameter name, the parameter is
# assigned to the list underneath.
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    print("\nGreeting each user:")
    for name in names:
        msg = f"Hello {name.title()}, welcome to the program!"
        print(msg)

# List of user names.
user_names = ["peter", "frank", "lucia", "stinus",]

# Calling function and asigning values to parameter, name.
greet_users(user_names)


def design_in_progress(unprinted_designs, completed_designs):
    """
    Getting each design, then moving it to in progress, 
    from there; we move it to the list that has every completed design.
    """
    # Simulate printing each design, until non are left.
    print("\nShowing each design in progress:")
    while unprinted_designs:
        printing_design = unprinted_designs.pop()
        print(f"Printing design: {printing_design}")  

        # Move each design to the empty list when completed.
        # Simulate creating a 3d print from the design.
        completed_designs.append(printing_design)

def complete_in_list(completed_designs):
    """Showing each completed design in the form of a list."""
    print("\nHere follows each completed design:")
    for completed_design in completed_designs:
        print(f"- {completed_design.title()}")

# Start with some designs that need to be printed.
unprinted_designs = ["lunch box", "water bottle", "iphone phone case", "gun"]
completed_designs = []

# Calling both functions.
design_in_progress(unprinted_designs, completed_designs)
complete_in_list(completed_designs)


def get_new_users(new_users, user_data_base):
    """
    Getting each new user out of list then displaying each new user by name.
    When displayed moving it to the user data base list.
    """
    # Showing each new user.
    print("\nShowing each new user:") 
    while new_users:
        new_user = new_users.pop()
        print(f"New user: {new_user.title()}")

        # Move each user to user_base.
        user_data_base.append(new_user)

def show_user_data(user_data_base):
    """Displaying each new user in a list."""
    print("\nShowing each new user:")
    for user in user_data_base:
        print(f"- {user.title()}")

# Moving new users to user base.
new_users = ["lukas", "coone", "franky", "petronel", "danique",]
user_data_base = []

# Calling each function, with parameters asigned to it. 
# 
# If parameters not called, function won't work.
get_new_users(new_users, user_data_base)
show_user_data(user_data_base)