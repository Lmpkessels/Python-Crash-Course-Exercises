# Storing file in a variable called, name_file.
name_file = ("/Users/luukkessels/Documents/Books - Python/Chapter_10/"
             "pi_million_digits.txt")

# Here we open the file.
with open(name_file) as million_digits:
    # Here we read each line withing the file, and assign it to digits.
    digits = million_digits.readlines()

# Here we create a empty string.
s_lines = ''
# We loop trough digit in digits to get each digit.
for digit in digits:
    # Assigning empty string to digit.
    s_lines += digit.strip()

# We create a variable called birthday to get user input and check if the 
# birthday of the user appears in the first million digits of py.
birthday = input("See if your birthday appears in the first million digits," 
                 "enter your birthday in mmddyy: ")

# Here we tell the program what to do if the input of user (which is birthday) 
# is found within the first million digits.
# 
# Else if it's not found print...
if birthday in s_lines:
    print("Your birthday appears in the first million digits of py!")
else:
    print("Your birthday doesn't appear in the first million digits of py!")