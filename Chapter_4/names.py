# Declaring a list of friends
names = ["Koen", "Lude", "Siem", "Mike"]

# Calling each name
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# Greeting each name
print(f"Hello {names[0]} great to see you again!")
print(f"Hello {names[1]} great to see you again!")
print(f"Hello {names[2]} great to see you again!")
print(f"Hello {names[3]} great to see you again!")

# Calling each name with a for loop
for name in names:
    print(name)

# Greeting each name with a for loop
for name in names:
    print(f"Hello {name} great to see you again!")

# Declaring a list of motorcycles
motorcycles = ["Husqvarna", "Kawasaki", "KTM", "Ducati"]

# Telling something about each motor
print(f"I've owned a working {motorcycles[0]} in the past.")
print(f"The {motorcycles[1]} is a green motorcycle.")
print(f"You have multiple versions of {motorcycles[2]} such as crossmotors.")
print(f"{motorcycles[3]} is a fast racemotor")

# Calling each motor with a for loop
for motor in motorcycles:
    print(f"This is a {motor}")