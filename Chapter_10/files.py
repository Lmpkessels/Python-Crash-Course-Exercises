# This is an absolute file path python can read this no-matter were it is stored
# in the computer.
#
# We have assigned it to a variable so it's name is shorter and more readable 
# when were opening it.
file_path = ("/Users/luukkessels/Documents/Books - Python/Chapter_10/"
"pi_digits.txt")

# Here we open the file, with makes sure the the document or path gets opened
# and closed, you could use open(), and close(), but this can cause bugs.
# 
# We use as to assign the open to objects then, we read the file then,
# we print the file through the variable we have assigned to is.
#
# We use rstrip() to strip unessesary white space.
with open(file_path) as file_object:
    objects = file_object.read()
    print(objects.rstrip())


# Here we use a for loop to get the data stored within this file, line-by-line.    
print("\n")
with open(file_path) as file_obj:
    for line in file_obj:
        print(line)