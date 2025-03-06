### Passing a List ###
# Function for message to users.
def greet_users(names):
    """Greeting each user in the list."""
    for name in names:
        msg = (f"Hello {name.title()}!")
        print(msg)

# Declaring list of users.
user_list = ["anja", "koen", "johan", "luuk"]

# Greeting users.
greet_users(user_list)


### Modifying a List in a Function ###
# Start with some design that need to be printed, define a unprinted and 
# printed list.
unprinted_designs = ["apple case", "lunch box", "gun", "bottle",]
printed_designs = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    printed_design = unprinted_designs.pop()

    # Simulate creating a 3D print from the design.
    print(f"Printed design: {printed_design.title()}")
    printed_designs.append(printed_design)

# Displaying each model that is created.
for printed_model in printed_designs:
    print(printed_model.title())


# A list of ordered candy, that is going to be moved to chipped candy.
ordered_candy = ["M&M's", "snickers", "twix", "maltasers",]
chipped_candy = []

# Moving ordered candy to order.
while ordered_candy:
    order = ordered_candy.pop()

    # Showing each ordered candy.
    print(f"Ordered candy: {order.title()}")
    
    # Moving to chipped candy, so we can chip it.
    chipped_candy.append(order)


# Showing each candy that's been chipped.
print("\nThe following orders have been chipped:")
for candy in chipped_candy:
    print(candy.title())


# Function for items 
def print_models(unprinted_designs, completed_designs):
    """
    Simulate printing each design until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        designs = unprinted_designs.pop()
    
        # Printing each printed design.
        print(f"Printed designs: {designs}")

        # Moving each completed item to completed designs.
        completed_designs.append(designs)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Two lists whan with unprinted items that need to be processed, the 
# other for completed items.
unprinted_designs = ["apple case", "lunch box", "gun", "bottle",]
completed_designs = []

# Showing functions (this one i forgot, always show functions otherwise 
# nothing will be displayed.)
print_models(unprinted_designs, completed_designs)
show_completed_models(completed_designs)