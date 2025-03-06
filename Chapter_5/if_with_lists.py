### Checking for Special Items ###

# Toppings asked by the customer
requested_toppings = ["chocolate", "cherry's", "nuts"]

# What to do as stag while topping is requested
#
# Using a for loop that asks for requested_topping in requested_toppings
# so the staff knows what to do when requested.
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")

# Telling customer ice cream is ready
print("Your ice cream is ready!")

# Telling the customer why they can't have chocolate if they ask for it
#
# Telling the customer that we adding topping's they've asked for
for requested_topping in requested_toppings:
    if requested_topping == "chocolate":
        print("Sorry for today chocolate is out of stock"
        ", tommorow we have new stock.")
    else:
        print(f"Adding {requested_topping}")

# Telling the cutomer that the Ice Cream is finished.
print("Finished your Ice Cream, enjoy it!")


### Checking That a List Is Not Empty ###

# An empty list to gather user input
requested_toppings = []

# Understanding what to do with requested toppings
#
# If no requested toppings asking customer if they are sure they want
# a plain pizza.
if requested_topping:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    else:
        print("Are you sure you want a plain pizza?")


# List with available toppings at the pizzaria
available_toppings = ["extra cheese", "olives", "peper", "sause", "extra meat",
"mushrooms"]

# List of requested toppings by user
requested_toppings = ["extra cheese", "olives", "extra meat", "sause"]

# Checking if requested topings are in stock - if not, we tell the
# customer were sorry.
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")

# Telling customer pizza is in progress
print("Finishing your pizza!")