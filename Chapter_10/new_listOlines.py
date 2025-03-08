# Creating a store for 'pi_digits.txt' file.
digits_file = ("/Users/luukkessels/Documents/Books - Python/Chapter_10/"
               "pi_digits.txt")

# Opening file.
with open(digits_file) as open_file:
    # Reading each line and putting it into a list.
    lines = open_file.readlines()

# Creating a list of content within file. We use an empty string to store content 
# in one line.
s_digits = ''
s_ddigits = ''
# Getting each line-by-line.
for line in lines:
    # We assign the empty string to each line, now each line gets placed within 
    # the string, this creates a kind of list form, BUT IT IS A STRING.
    # 
    # We use rstrip to strip each invisible white line with puts behind each 
    # line after opening the file.
    s_digits += line.rstrip()
    # We can use strip to strip all white space.
    s_ddigits += line.strip()

# We print the string.
print(s_digits)
print(s_ddigits)

# We check how many characters there are in this list.
#
# We check how long the string is.
print(len(s_digits))
print(len(s_ddigits))