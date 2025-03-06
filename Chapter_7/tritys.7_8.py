### Excersise 7-8, Deli ###
# A list of ordered sandwhiches, and a list for finished sandwhiches
sandwhich_orders = ["fried chicken", "kebab", "cheese", "shoarma",]
finished_sandwhiches = []

# We use a while loop to access the sandwhich_orders_2 list and loop 
# through it, then we create a variable and assign every item in the 
# list to it.
# 
# Then we print a sentence in where we declare that the sandwhich has 
# been finished.
while sandwhich_orders:
    sandwhich = sandwhich_orders.pop()
    print(f"I made you a {sandwhich.title()} sandwhich!")

    # Here we append the items we have assigned to sandwhich_2 to the
    # finished_sandwhiches_2 list.
    finished_sandwhiches.append(sandwhich)
    print(finished_sandwhiches)

    # And here we decclare every sandwhich had been made with a for loop.
    for finished in finished_sandwhiches:
        print(f"The {finished.title()} sandwhich has been made!")

    
### Excersise 7-9, No Pastrimi ###
# List of ordered sandwhiches, then empty list to moved finished, 
# sandwhiches.
sandwhich_orders = ["fried chicken", "pastrami", "kebab", "pastrami", 
"cheese", "shoarma", "pastrami"]
finished_sandwhiches = []

# Telling the customer we've run out of pastrami.
print(f"Sorry but we run out of {sandwhich_orders[0]}")

# Removing pastramin from order list.
while "pastrami" in sandwhich_orders:
    sandwhich_orders.remove("pastrami")

# Telling customer sandwhich is ready.
while sandwhich_orders:

    sandwhich = sandwhich_orders.pop()
    print(f"I made your {sandwhich.title()} sandwhich.")

    # Moving items from sandwhich_orders to finished_sandwhiches.
    finished_sandwhiches.append(sandwhich)
    print(finished_sandwhiches)

# Printing a message for every sandwhich that has been made.
for sandwhich in finished_sandwhiches: 
    print(f"{sandwhich.title()} has been made!")

# Listing each sandwhich that's been made.
print(f"Here's a list of each sandwhich that is been made",
       f"{finished_sandwhiches}")


### Excersise 7-10, Dream Vacation ###
# Dictionary for poll.
answers = {}

# Set a flag to indicate that polling is active.
poll_active = True

while poll_active:
    # Prompt for the person's name and respone.
    name = input("\nWhat is your name? ")
    answer = input(f"{name} if you could visit one place in the world,"
                    " where would you go? ")

    # Store the response in the dictionary
    answers[name] = answer

    # Find out if anyone else is going to take the poll.
    anyone_else = input(f"{name} do you have anyone else who is going" 
                        f"to take the poll, please answer (yes/ no). ")
    # Instead of anyone_else == "no" or "No" or "NO" - Just use 
    # .lower() == "no"
    if anyone_else.lower() == "no":
        poll_active = False

# Polling is complete show the results
print("\n--- Results Poll ---")
for name, answer in answers.items():
    print(f"{name.title()} would like to visit {answer.title()}.")