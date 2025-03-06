# Here is a list of my favorite food from 1 to 4
my_food = ["Rib eye", "Drumsticks", "Pizza", "Pasta bolognese"]
# Generating my first three favorite foods
print("The first three items in the list are", my_food[0:3])
# Genrating second and third favorite food
print("The three items in the midle of my list are", my_food[1:3])
# Generating my last three favorite foods
print("The last three items in the list are", my_food[1:])

# Here is a list with my favorite pizza from 1 to 3
my_pizzas = ["Self made", "Magarita", "Shoarma"]
# Here I say that I like {name} of the pizza in 3 sentences
for name in my_pizzas:
    print(f"\nI like {name} pizza.")
# Here I say that I like pizza very much
print("\nI like pizza very much!")

# Here I copy my list and make a list for my friend
friends_pizzas = my_pizzas[:]
# Adding an item to my list
my_pizzas.insert(0, "Kebab")
# Adding an item to my friends list
friends_pizzas.insert(0, "Peporoni")

# Saying my favorite pizza's are followed by my favorite pizza's
print("\nMy favorite pizza's are:")
print(my_pizzas)
print(f"\nMy favorite pizza's are: {my_pizzas}")

# Saying my friend favorite pizza's are followed by my friend favorite pizza's
print("\nMy friends favorite pizza's are:")
print(friends_pizzas)
print(f"\nMy friends favorite pizza's are: {friends_pizzas}")

# Looping 3 times my favorite pizza's are: followed by name
for pizza in my_pizzas:
    print("\nMy favorite pizza's are:", pizza)

# Looping 3 times my friends favorite pizza's are: followed by name
for pizza in friends_pizzas:
    print("\nMy friends favorite pizza's are:", pizza)

# Only generating names of my favorite pizza's
for pizza in my_pizzas:
    print(pizza)

# Only generating names of my friends favorite pizza's
for pizza in friends_pizzas:
    print(pizza)