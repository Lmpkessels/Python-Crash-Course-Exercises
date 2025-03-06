# Pizza talking program
# List of great pizza's
my_pizzas = ["Peporoni", "Shoarma", "Mixed grill", "Kebab", "Hawaii"]

# Telling something about each pizza
for pizza in my_pizzas:
    print(f"\nPizza {pizza} is a great choice!")
    print(f"I like pizza", pizza)

# What I think of pizza in general
print("\nI like pizza!")

# Excersise 4-10
# (The item starts literally from the number so 1 is item 1 in the list)
# Stating what the first three items in the list are
print(f"\nThe first three items in the list are", my_pizzas[0:3])
# Showing three items starting from the middle of my list
print(f"Three items from the middle of my list", my_pizzas[2:])
# Giving a message of the last three items in my list
print(f"The last three items of my list are", my_pizzas[-3:])

# Coppying my list of pizzas to a new list of my friends pizzas
# [:] is used to create two different lists 
friend_pizzas = my_pizzas[:]
# Checking if the list is coppied
print(friend_pizzas)

# Adding a pizza I like more
my_pizzas.insert(0, "Chicken")
print(my_pizzas)

# Adding a pizza my friend likes more
friend_pizzas.insert(0, "Magarita")
print(friend_pizzas)

"""
Create this one in the right order how it supposed to be the next time you code,
before you do anything else. Also do -> excersise 4-12 More loops; page 69.
"""

# Excersise 4-11 My pizzas, your pizzas
# Showing what my favorite pizza's are
for pizzas in my_pizzas:
    print(f"My favorite pizza's are:", my_pizzas)
    print(f"My favorite pizza's are: {my_pizzas}")

# Showing what my friends favorite pizza's are
for pizzas in friend_pizzas:
    print(f"My friend favorite pizza's are:", friend_pizzas)
    print(f"My friend favorite pizza's are: {friend_pizzas}")