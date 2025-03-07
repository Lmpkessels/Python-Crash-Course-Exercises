from collections import OrderedDict
from random import randint

glossary = OrderedDict()

glossary["loop"] = "go through each statements till all statements are met to" 
" be true."
glossary["function"] = "write clean, re-usable, effective code."
glossary["class"] = "create a bigger picture of for example a car."
glossary["items"] = "access a dictionary."
glossary["pop"] = "get items out of a dictionary."

print("\n")
for name, description in glossary.items():
    print(f"{name.title()} is used to {description}")


class Die():
    """"""
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        """"""
        return randint(1, self.sides)
    
d6 = Die()

results = []

for rolled_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("Displaying 10 numbers in a range of 6")
print(results)


d10 = Die(sides=10)

results = []
for rolled_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("Displaying 10 numbers in a range of 10")
print(results)


d20 = Die(sides=20)

results = []
for rolled_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("Displaying 10 numbers in a range of 20")
print(results)