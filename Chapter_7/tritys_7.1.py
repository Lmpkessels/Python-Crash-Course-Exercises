# Asking user what car he would like to rent
# 
# Telling him/her were checking if the car is available
rental_car = input("Tell us what rental car would you like? ")
print(f"Let me see if we can find you a {rental_car}!")


# Asking how much people are in dinner group, then telling what to do
# if they're with more then eight
question = int(input("Hello, with how much people are you guys? "))
if question > 8:
    print("Sorry guys, you'll have to wait till a table is available.")
else:
    print("Your table is ready, follow me!")


# Asking user for a number, when received checking if number is even or 
# odd
number_check = int(input("Give me a number, then I check if it's even" 
                         " or odd: "))

# Checking if input is odd or even
if number_check % 2 == 0:
    print(f"The number {number_check} is even!")
else:
    print(f"The number {number_check} is odd.")


# Asking for a number and checking if it is a multiple of 10 or not
number_check_1 = int(input("Give me a number then I'll check if it is a" 
                           " multiple of ten or not: "))

# Checking if number is a mutliple of 10 or not
if number_check_1 %10 == 0:
    print(f"The number {number_check_1} is a multiple of ten.")
else:
    print(f"The number {number_check_1} is not a multiple of ten.")