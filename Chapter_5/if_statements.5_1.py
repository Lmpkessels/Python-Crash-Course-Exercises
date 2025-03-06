# Telling that the grass is green
grass = "green"

# Printing a statemenet that the grass is green in upper case
if grass == "green":
    print(f"The grass is {grass.upper()}!")


# Checking if person is old enought to drive
age = 17

# Sending a message that he/she is old enough to young
if age >= 18:
    print("You are old enough to drive")
    print("You are old enough to vote")
else:
    print("You are to young to drive")
    print("You are to young to vote")


# Price list for amusement park
age = 67

# Telling the visitor what the price is depending on their age
if age < 4:
    print("age 4 is FREE!")
elif age < 18:
    print("Between age 4 and 18 cost $5,-")
elif age < 65:
    print("Age 18+ cost $10,-")
else:
    print("Age 65+ costs $5,- ")


# Creating a pizza
pizza_topping = ["mushrooms", "olives", "unions", "bell pepper"]

# Using logical IF operator to check if multiple conditions in the list
# are true.
#
# When True telling my staf what to put on the pizza
if "mushrooms" in pizza_topping:
    print("Add Mushrooms to the pizza!")
if "olives" in pizza_topping:
    print("Add Olives to the pizza!")
if "unions" in pizza_topping:
    print("Add Unions to the pizza!")
if "bell pepper" in pizza_topping:
    print("Add Bell Peper to the pizza!")
if "sambal" in pizza_topping:
    print("Add Sambal to the pizza!")

# Telling the customer pizza is ready
print("\nYour pizza is ready, enjoy your meal!")