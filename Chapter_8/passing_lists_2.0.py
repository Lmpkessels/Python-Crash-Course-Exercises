# Define a function called greet_users().
def greet_users(user_list):
    """Greeting each user in the list."""
    for user in user_list:
        msg = f"Hello {user.title()}!"
        print(msg)

# Create a list with users.
user_list = ["koen", "johan", "anja", "luuk"]

# Get out the message.
greet_users(user_list)


### Modifying a list in a function ###

### This is the only code that is added to the program to declare the 
# function.
def print_models(unprinted_designs, printed_designs,):
    """
    Sumulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    ###

    # Moving items to variable ready.
    while unprinted_designs:
        designs_ready = unprinted_designs.pop()

        # Showing which designs are in print.
        print(f"\nPrinting model: {designs_ready.title()}")

        # Assigning printed items to list that's ready.
        printed_designs.append(designs_ready)

### This is the only code that is added to the whole program to declare 
# functions.
def show_printed_designs(printed_designs):
    """Show all the models that where printed."""
    ###

    print("\nThe following models have been printed:")
    for design in printed_designs:
        print(design.title())

# Start with some designs that need to be printed.
unprinted_designs = ["lunch box", "drink bottle", "tortilla box", 
"phone case",]
printed_designs = []

# Here we call both functions, this NEEDS to be added otherwise the 
# functions won't work.
#
# What we do is simply put the name of the function, then we call the 
# parameters in the function.
print_models(unprinted_designs, printed_designs)
show_printed_designs(printed_designs)


### Modifying a list in a Function ###
# 

# Designs that need to be printed.
unprinted_designs = ["iphone case", "samsung case", "water bottle", 
"lunch box",]

# Designs that are printed.
completed_designs = []