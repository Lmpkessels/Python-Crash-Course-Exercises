# Guest list for dinner party
guest_list = ["Johan", "Anja", "Koen", "Lude", "Mike", "Elon", "Donald"]

# Creating a variable to store the name of each invited person
guest_1 = guest_list[0]
guest_2 = guest_list[1]
guest_3 = guest_list[2]
guest_4 = guest_list[3]
guest_5 = guest_list[4]
guest_6 = guest_list[5]
guest_7 = guest_list[6]

# Sending an invitation to each person
print(f"{guest_1}, you are invited to my dinner party!")
print(f"\n{guest_2}, you are invited to my dinner party!")
print(f"\n{guest_3}, you are invited to my dinner party!")
print(f"\n{guest_4}, you are invited to my dinner party!")
print(f"\n{guest_5}, you are invited to my dinner party!")
print(f"\n{guest_6}, you are invited to my dinner party!")
print(f"\n{guest_7}, you are invited to my dinner party!")

# Sending an invitation to each person with the use of a for loop so I 
# 
# don't need to write so much
for guest in guest_list:
    print(f"\n{guest} you are invited to my dinner party!")

# Excersis 3-4 Changing Guest List:
# We already declared this name so...
print(
    f"\n{guest_4}, unfortunatly couldn't make it to the dinner" 
    "party!"
    )

# Person(s) who canceled
canceled = guest_list.pop(3)
print(
    f"""\n{canceled}, unfortunatly couldn't make it to the dinner 
    party!\n"""
    )

# Inviting a new person to the dinner party because of cancelation
guest_list.insert(3, "Epictetus")
print(guest_list)

# Inviting all new people to the dinner party
print(f"\n{guest_list[0]}, you are invited to my dinner party!")
print(f"\n{guest_list[1]}, you are invited to my dinner party!")
print(f"\n{guest_list[2]}, you are invited to my dinner party!")
print(f"\n{guest_list[3]}, you are invited to my dinner party!")
print(f"\n{guest_list[4]}, you are invited to my dinner party!")
print(f"\n{guest_list[5]}, you are invited to my dinner party!")
print(f"\n{guest_list[6]}, you are invited to my dinner party!")

# Inviting all new people do the dinner party with a for loop
for guest in guest_list:
    print(f"\n{guest}, you are invited to my dinner party!\n")

# Excersise 3-6 More Guests:
guest_list.insert(0, "John")
guest_list.insert(5, "Karel")
guest_list.append("Peter")

# Inviting more people
guest_0 = guest_list[0]
guest_1 = guest_list[1]
guest_2 = guest_list[2]
guest_3 = guest_list[3]
guest_4 = guest_list[4]
guest_5 = guest_list[5]
guest_6 = guest_list[6]
guest_7 = guest_list[7]
guest_8 = guest_list[8]
guest_9 = guest_list[9]

# Checking if everything works
print(guest_list)

# Hard coding invitations
print(f"\n{guest_0}, you are invited to my dinner party!")
print(f"\n{guest_1}, you are invited to my dinner party!")
print(f"\n{guest_2}, you are invited to my dinner party!")
print(f"\n{guest_3}, you are invited to my dinner party!")
print(f"\n{guest_4}, you are invited to my dinner party!")
print(f"\n{guest_5}, you are invited to my dinner party!")
print(f"\n{guest_6}, you are invited to my dinner party!")
print(f"\n{guest_7}, you are invited to my dinner party!")
print(f"\n{guest_8}, you are invited to my dinner party!")
print(f"\n{guest_9}, you are invited to my dinner party!")

# Printing new invitations to everyone including the new guests
for name in guest_list:
    print(f"\n{name}, you are invited to my dinner party!\n")

# Excersise 3-7 Shrinking Guest List
# Canceling most people
print(
    """The restaurant called me I there is only a table available for
    three, so I only can invite two people\n"""
    )

# Taking guests who cant come out of the list
guest_0 = guest_list.pop(0)
guest_3 = guest_list.pop(3)
guest_4 = guest_list.pop(4)
guest_5 = guest_list.pop(-5)
guest_6 = guest_list.pop(-4)
guest_7 = guest_list.pop(-3)
guest_8 = guest_list.pop(-2)
guest_9 = guest_list.pop(-1)

# Sending them a excuse message which cancels their invitation
print(f"""\n 
    {guest_0} I'm sorry to tell but you can't come to the dinner party!
    """)
print(f"""\n 
    {guest_3} I'm sorry to tell but you can't come to the dinner party!
    """)
print(f"""\n 
    {guest_4} I'm sorry to tell but you can't come to the dinner party!
    """)
print(f"""\n 
    {guest_5} I'm sorry to tell but you can't come to the dinner party!
    """)
print(f"""\n
    {guest_6} I'm sorry to tell but you can't come to the dinner party!
    """)
print(f"""\n
    {guest_7} I'm sorry to tell but you can't come to the dinner party!
    """)
print(f"""\n
    {guest_8} I'm sorry to tell but you can't come to the dinner party!
    """)
print(f"""\n 
    {guest_9} I'm sorry to tell but you can't come to the dinner party!
    """)

# Testing new guest list
print(guest_list)

# Sending invitation to the two people who can still come
print(f"\n{guest_1}, you are still invited to my dinner party, till then.")
print(f"\n{guest_2}, you are still invited to my dinner party, till then.")

# Sending invitation to the two people who can still come with a for loop
for guest in guest_list:
    print(f"\n{guest}, you are still invited to my dinner party, till then.")

# Cleaning guest list
del guest_list[0]
del guest_list[-1]

# Checking if guest list is clean
print(guest_list)

# Excersise 3-9 Dinner Guests
# Checking length of guest_list
print(len(guest_list))