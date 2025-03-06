"""
Coding try it yourself - Guest list.
Always use #Notes!!!! Be CLEAR.
"""

#Starting the program.
#Here I create a list that include people I want to invite to my dinner party.
invite_list = ["Johan", "Anja", "Koen", "Lude", "Mike"]

#Here I use the (len) to see how much people I have invited.
print(len(invite_list))

#This was unecessary it made the code longer - now it is done faster. 
"""#Assigning every person in the list to a specific string.
name_johan = invite_list[0]
name_anja = invite_list[1]
name_koen = invite_list[2]
name_lude = invite_list[3]
name_mike = invite_list[4]
"""

#Creating a specific invite message for every person.
print(f"Hello {invite_list[0]} on 23-02-2025 are you invited to my dinenr party, till then!"
f"\nHello {invite_list[1]} on 23-02-2025 are you invited to my dinenr party, till then!"
f"\nHello {invite_list[2]} on 23-02-2025 are you invited to my dinenr party, till then!"
f"\nHello {invite_list[3]} on 23-02-2025 are you invited to my dinenr party, till then!"
f"\nHello {invite_list[4]} on 23-02-2025 are you invited to my dinenr party, till then!")

#This print function is used to print a message of the person who couldn't be there.
print(f"Unfortunately {invite_list[3]} be at the dinner party because he needed to run his business.")

#Removing the person from the list.
invite_list.pop(3)

#Inserting the peter into the invite list.
invite_list.insert(3, "Peter")

#Assinging a variable of the new invited person to list item 3
name_peter = invite_list[3]

#Specific invite message with the new person.
print(f"Hello {invite_list[0]} on 23-02-2025 are you invited to my dinenr party, till then!"
f"\nHello {invite_list[1]} on 23-02-2025 are you invited to my dinenr party, till then!"
f"\nHello {invite_list[2]} on 23-02-2025 are you invited to my dinenr party, till then!"
f"\nHello {invite_list[3]} on 23-02-2025 are you invited to my dinenr party, till then!"
f"\nHello {invite_list[4]} on 23-02-2025 are you invited to my dinenr party, till then!")

#I found a larger table, so here I add new people to the list
invite_list.insert(0, "Karel")
invite_list.insert(3, "John")
invite_list.append("Freek")

#This is a message for the new people that are invited to the dinner party.
print(f"Hello {invite_list[0]} on 23-02-2025 are you invited to my dinenr party, till then!"
f"\nHello {invite_list[3]} on 23-02-2025 are you invited to my dinenr party, till then!"
f"\nHello {invite_list[7]} on 23-02-2025 are you invited to my dinenr party, till then!")

#Printing a message to excuse me because only a table for two is available.
print(f"Hey guys, the restaurant called me and I can only invite two people for the dinner party, because there is only a table of three available so I go with my mom and dad")

#Here I'm popping the guests who I can't invite anymore and leave them a message.
print(f"Hello {invite_list.pop(0)} I'm sorry but I can't invite you for the dinner, next time.",
f"\nHello {invite_list.pop(2)} I'm sorry but I can't invite you for the dinner, next time.",
f"\nHello {invite_list.pop(3)} I'm sorry but I can't invite you for the dinner, next time.",
f"\nHello {invite_list.pop(4)} I'm sorry but I can't invite you for the dinner, next time.",
f"\nHello {invite_list.pop(-2)} I'm sorry but I can't invite you for the dinner, next time.",
f"\nHello {invite_list.pop(-1)} I'm sorry but I can't invite you for the dinner, next time.")

#Here the people who are allowed to come get a new message.
print(f"Hello {invite_list[0]} you can come to my dinner party because, you're my dad"
f"\nHello {invite_list[1]}  you can come to my dinner party because, you're my mom")

#Here I make sure my invite list is clean.
name_0 = "Johan"
name_1 = "Anja"
invite_list.remove(name_0)
invite_list.remove(name_1)
print(invite_list)

#Here I use the (len) to see if the invite list is cleared.
print(len(invite_list))