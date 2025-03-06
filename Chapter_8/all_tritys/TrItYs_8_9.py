### Excersise 8-9, Magicians ###
# Using a function to show each name of the magician.
def show_magicians(names):
    """Displaying each magician by name."""
    for name in names:
        print(name.title())

def make_great(great):
    """Getting The Great in front of each magician."""
    for make in great:
        print(f"the Great {make.title()}.")

# List of magicians.    
magician_names = ["harry houdini", "david copperfield", "steven frayne", 
                  "penn & teller", "shin lim"]

# Calling function.
show_magicians(magician_names)
make_great(magician_names)


