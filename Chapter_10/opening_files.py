# Assigning variable to file path.
file_path = ("/Users/luukkessels/Documents/Books - Python/Chapter_10/"
             "pi_digits.txt")

# Opening file in its whole.
with open(file_path) as gaining_access:
    access = gaining_access.read()
    print(access)

print("\n")

# Opening file line by line.
with open(file_path) as line_by_line:
    for line in line_by_line:
        print(line)

print("\n")

# Opening file line by line, but because we use rstrip(); the lines will fit
# together and become a whole again.
#
# We have those white spaces because with has invisible white space at the back
# of each file. (if i'm understanding it right.)
with open(file_path) as lines:
    for line in lines:
        print(line.rstrip())


