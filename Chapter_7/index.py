# Fast and clear, but less specific, here we don't tell why we want 
# the input
name = input("\nPlease enter your name: ")
print("\nHello", name)

# Here we are a bit more specific we first tell the user why we ask them 
# what their name is and then we ask for the name we do this by using 
# the += operator to ad multiple sentences
promt = "\nIf you tell us your name, then we can personalize the message" 
" you see."
promt += "\nWhat is your name? "

# Message to the user
name = input(promt)
print(f"\nHello {name}!")


# Here we ask the user for their age we use INT so the program can also 
# use numbers
age = int(input("\nHow old are you? "))
if age < 18:
    print("\nYou are to young to drive!")
elif age >= 18:
    print("\nYou are allowed to drive!")


# Telling the user if a number is even or odd
number = input("\nTell me a number, and I tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even!")
else:
    print("\nThe number " + str(number) + " is odd!")


# How it can be done faster based on my experience
number = int(input("\nTell me a number, and I tell you if it is even or" 
" odd: "))

# Checking if number input is even or odd
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even!")
else:
    print("\nThe number " + str(number) + " is odd.")

# Greeting the user goodbye
print(f"\nThank you {name} for using the program, have a nice day!")

