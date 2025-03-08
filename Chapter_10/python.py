# Create variable to store file.
name_file = ("/Users/luukkessels/Documents/Books - Python/Chapter_10/"
             "learning_python.txt")

# Getting acces to the file, and then read the file.
with open(name_file) as learning_python:
    learning = learning_python.read()


# Reading each line, line-by-line.
with open(name_file) as l_python:
    learning = l_python.readlines()

# We use a for loop to get each line, by-line. 
# With, has an invisible line when opening files. 
# This is also the reason why we use rstrip.
for learned in learning:
    learned = learned.rstrip()
    # Printing learned.


# Here again we open file as learning_python_py.
with open(name_file) as learning_python_py:
    # We create a variable to read each line, line-by-line.
    learning_pyth = learning_python_py.readlines()

# We assign a empty string so we can create a list.
st_learning_py = ''

# For learned in learning python, add learned to st_learning_py which 
# creates a kind of list form.
for learned in learning_pyth:
    st_learning_py += learned.strip()


# Here we open the file, then we assign it to learning_py.
with open(name_file) as learning_py:
    # We create a variable to read each line, line-by-line.
    lines = learning_py.readlines()

# Assigning an empty string to variable.
s_lines = ''

# Accessing each individual line.
for line in lines:
    # Assigning each individual line to string.
    s_lines += line
    # Replacing word python with java by using method replace.
    #
    # We need to create a new variable to get access to the method, replace().
    new_s_lines = s_lines.replace("python", "java")

# Printing new context, instead of python we see now javascript.
print(new_s_lines)

# Printing unmodified context, here we see python as displayed in the document, 
# learning_python.txt.
print(s_lines)