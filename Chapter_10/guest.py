# Creating a variable to write clean code.
guest_file = "/Users/luukkessels/Documents/Books - Python/guest.txt"

# Asking user for their name, and to tell something about themselves.
user_input = input("Please provide your name: ")
about_yourself = input("Please tell us something about you hobbies: ")

# Here we move their input to a text file so we can store it's data.
with open(guest_file, "w") as guest:
    guest.write(user_input)
    guest.write(f"\n{about_yourself}")