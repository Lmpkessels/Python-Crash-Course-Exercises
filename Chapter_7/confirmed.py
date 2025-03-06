# Start with users that need to be verified, and an empty list to hold
# confirmed users.
#
# Creating an list with unconfirmed users, and a empty list for confirmed 
# users.
unconfirmed_users = ["erik", "john", "franky",]
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of verified users.
#
# Here we use a while loop to get into the list, then we create a 
# variable called current_user and assign it to unconfirmed_users.pop()
# so we can take the values out of the list.
#
# Then we use a print statement to say that we are verifying users we 
# assign the variable current_user to it, the we put together with
# .append confirmed_users.append(current_user)
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed user.
#
# We send a message to make clear what is coming next -> the following 
# users.
#
# We use a for loop to get the confirmed_user out of the list 
# confirmed_users, then we print the confirmed users .title() so it starts 
# with a capital letter.
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# Removing a specific value from a list
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

# Here we remove cat from pets by using the function .remove().
#
# We use the while loop (while cat in pets remove cat) that's what's 
# standing there.
# 
# The while loop loops through the list to look for "cat"
while "cat" in pets:
    pets.remove("cat")

# Here we print the new list without cats.
print(pets)

# Here we do the same but then with dog.
while "dog" in pets:
    pets.remove("dog")

print(pets)


# An empty dictionary
responses = {}

# Creating a flag that sets polling_active to True, with a flag we can 
# make sure a loop stops when a specific value is typed in by the user
# (if I'm right).
polling_active = True

# We create a while loop to gather data from the user input this loop,
# loops through the questions that follow.
while polling_active:
    name = input("\nWhat is your name? ")
    response = input(f"{name.title()} which mountain would you like to climb" 
                     " someday? ")

    # Here we add name to the responses dictionary which becomes the 
    # response.
    responses[name] = response


    # Here we ask the user if he would like to let someone else fill in 
    # the poll.
    repeat = input("Would you like to let another person respond?" 
                   " (yes/ no) ")
    if repeat == "no" or "No" or "NO":
        polling_active = False

    # Here we put out the message of the poll and then we say who would 
    # like to climb what mountain   
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")