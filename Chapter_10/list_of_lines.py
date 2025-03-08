# Creating a shorter name for file path by using a variable.
stored_file = ("/Users/luukkessels/Documents/Books - Python/Chapter_10/"
               "pi_digits.txt")

# We open the file we have stored in the variable stored_file. We use as to 
# assign it to digits_file.
with open(stored_file) as digits_file:
    # Taking each line from a file and storing it an a list, due to the 
    # method readlines.
    lines = digits_file.readlines()

# Pi_string creates a string so now the items of stored file will be places in 
# a list.
pi_string = ''
for line in lines:
    # Here we assign pi_string to line.
    pi_string += line.rstrip()

# We display pi_strip in the terminal.
print(pi_string)
# Here we look at the length by using len().
print(len(pi_string))