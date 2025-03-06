def show_magicians(magician_names):
    """Displaying the name of each magician."""
    print("\n")
    for magician in magician_names:
        print("- ", magician.title())

# List of magicians
magician_names = ["harry houdini", "david copperfield", "steven frayne", 
                  "penn & teller", "shin lim"]


def show_magicians(magicians):
    """Displaying the name of each magician."""
    print("\n")
    for magician in magicians:
        print("- " + magician.title())

def make_great(magicians):
    """Getting 'the Great' behind each magician."""
    # Creating an empty list for the_great magicians.
    the_great = []

    # Getting access to the list (magicians), then creating a variable, called;
    # magician which is assigned to the list but every name gets popped out. 
    # Then we create a variable for the graet. 
    # Then we append the great magicians to the empty list.
    while magicians:
        magician = magicians.pop()
        the_great_magician = f"{magician} the Great!"
        the_great.append(the_great_magician)

    # Here we get each magician with the great infront of it because we created 
    # this above.
    for great in the_great:
        print(great.title())

# List of magicians
magicians = ["harry houdini", "david copperfield", "steven frayne", 
            "penn & teller", "shin lim"]
show_magicians(magicians)

# Calling first make great, then show_magicians so that the list gets first 
# modified.
print("\n")
make_great(magicians)
show_magicians(magicians)


def show_magicians(magicians):
    """Displaying each magician by name."""
    for magician in magicians:
        print("- " + magician.title())

def make_great(magicians):
    """Getting 'the great' behind each magician."""
    # Creating a list to store the great magicians.
    the_great = []

    # Creating 'magician' the great.
    while magicians:
        magician = magicians.pop()
        the_great_magician = f"{magician.title()} the Great!"
        the_great.append(the_great_magician)

    # Displaying each the great + name.
    for great in the_great:
        magicians.append(great)

    # Returning each magician.
    #
    # Return is used to send back a value to the caller.
    return magicians

# List of magicians.
magicians = ["harry houdini", "david copperfield", "steven frayne", 
            "penn & teller", "shin lim"]

# Displaying the Great behind each magician.
print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

# Displaying original name, without anything added to it.
print("\nOriginal magicians:")
show_magicians(magicians)



def show_magicians(magicians_list):
    """Getting each individiual magician."""
    for magician in magicians_list:
        print("- " + magician.title())

def make_great(magicians_list):
    """Getting 'the Great' behind each magician."""

    the_great = []

    # Putting the great behind each mugician.
    while magicians_list:
        great_magician = magicians_list.pop()
        the_great_magician = f"{great_magician}, the Great"
        the_great.append(the_great_magician)

    # Getting each indivual magician, and appending it to magician list.
    for great in the_great:
        magicians_list.append(great)

    # Returning magician list.
    return magicians_list

# List of magicians.
magicians_list = ["harry houdini", "david copperfield", "steven frayne", 
            "penn & teller", "shin lim"]

# Calling list the great.
print("\nthe Great Magicians:")
g_magicians = make_great(magicians_list[:])
show_magicians(g_magicians)

# Displaying each magician by name.
print("\nNormal magicians:")
show_magicians(magicians_list)