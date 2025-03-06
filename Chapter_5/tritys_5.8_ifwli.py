### If with Lists ###
### Excersise 5-8, Hello Admin ###

# Users in this program
user_list = ["peter", "frank", "erik", "jan", "karel", "koen", "johan",
"anja", "luuk", "admin"]

# Greeting each user
for user in user_list:
    print(f"\nHello {user} and welcome to the program")

# Asking admin if he wants to see a status raport
#
# Thanking users for login in again
for user in user_list:
    if user == "admin":
        print("\nHello Admin would you like to see a status raport?")
    else:
        print(f"\nHello {user} thanks for logging in again!")


### Excersise 5-9, No Users ###

# Showing an empty user list
user_list = []

# Telling my staf that we need to find users
if user_list == []:
    print("We need to find some users")


### Excersise 5-10, Checking Usernames ###

# List of current users
current_users = ["peter", "frans", "nick", "karel", "erik", "koen"]

# List of new users
new_users = ["luuk", "koen", "anja", "johan", "nick", "LUUK"]

"""
Go on with excersise 5-10, STAY CALM! think about the problems that occur
and solve them don't overthink and look at the functionallity and what
the program should do. 

Good Luck!
"""

# Looping through current user list to see if user names are already
# used and which one not.
#
# Telling user if he can use the username or not
for user in new_users:
    if user in current_users:
        print(f"{user.title()} is already used, try another one!")
    elif user == user.upper():
        print(f"{user} is not accepted because its in upper!")


# Numbers one through nine
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Looping through list an printing each number with st, nd, th behind it
for number in list_numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    elif number == 4:
        print("4th")
    elif number == 5:
        print("5th")
    elif number == 6:
        print("6th")
    elif number == 7:
        print("7th")
    elif number == 8:
        print("8th")
    elif number == 9:
        print("9th")