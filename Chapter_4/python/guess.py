# Number confirtmation program
# Gathering user input
number = float(input("Enter a number: "))
# Confirming if number is positive negative or zero
if number > 0:
    print("This number is Positive")
elif number < 0:
    print("This number is Negative")
else:
    print("This number is Zero")
    break # Getting out of program