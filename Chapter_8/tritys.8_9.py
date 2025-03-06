### Excersise 8-9, Magicians ###
# Defining function with parameter of list magician names.
def show_magicians(magician_names):
    """Displaying each magician name."""

# Getting each name out of the list.
    for magician in magician_names:
        print(magician.title())

# List of magician names.
magician_names = ["harry houdini", "david copperfield", "dynamo", 
                  "penn jillette", "teller",]

# Calling the function.
show_magicians(magician_names)


### Excersise 8-10, Great Magicians ###
# Defining function with parameter of list magician names.
def show_magician(magician_names):
    """Displaying each magician name."""

    # Getting each magician by name.
    for magician in magician_names:
        print(magician.title())

# Define function to modify magician names and return a new list
def make_great(magician_names):
    """Return a new list with 'The Great' added to each magician name."""
    great_magicians = [f"The Great {magician.title()}" 
    for magician in magician_names]
    return great_magicians

# List of magician names
magician_names = ["harry houdini", "david copperfield", "dynamo", 
"penn jillette", "teller"]

# Create a new list with modified names (without changing original)
great_magicians = make_great(magician_names[:])  # Pass a copy of the list

# Display both lists
print("\nOriginal Magicians:")
show_magicians(magician_names)

print("\nGreat Magicians:")
show_magicians(great_magicians)