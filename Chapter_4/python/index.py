#Number guessing program.
#This variable holds the number to be guessed.
number = 12

#This while loop is used till the user guesses the right number.
while True:
    #Get the users input as a floating point number.
    number_i = float(input("What number am I holding: "))

    #Check if the guess is correct
    if number_i == number: 
        print("That's right! Nice job.")
        break #Exit the loop when the correct number is guessed.
    
    #Check if the guess number is lower then the correct number.
    elif number_i <= number:
        print("Try again, the number is higher.")

    #Check if the guess is higher than the correct number.
    else:
        print("Try again, the number is lower.")