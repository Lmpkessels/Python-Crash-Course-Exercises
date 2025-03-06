### Importing specific file functions ###
# Importing a function wich is won outside of a different file.
from pizza import make_pizza
# Assigning values to the parameters in the function (wich in this case
# are the toppings.)
make_pizza(16, "shoarma", "kebab", "champignons")

# Importing a function from a different file.
from pizza import make_person

# Asigning values, (wich in this case is the name) and callinng the 
# function.
make_person("luuk", "kessels")


### Using as to Give a Function an Alias ###
# An alias is often used for its readability, it's a nickname for if the
# name is used in the program already or if the name is long. We also 
# use it to avoid confusion.
#
# Example of using an alias.
#
# Using AS to create alias mp.
from pizza import make_pizza as mp

# Calling function.
mp(16, "champignons", "unions", "extra cheese")

# Using AS to create alias mp.
from pizza import make_person as mp

# Calling the function.
mp(name="luuk", last_name="kessels")


### Using as to Give a Module an Alias ###
# Asigning a alias to a module.
#
# What this allows us to do is call the function way faster then writing the,
# full word pizza.
import pizza as p

# Calling the function.
p.make_pizza(13, "peperoni", "extra cheese", "unions", "bell peper")
p.make_person("anja", "kessels")


### Importing All Function in a Module ###
# We use the asterisk statement to call each function, in the file pizza.
from pizza import *
make_pizza(16, "kebab", "unions", "garlic")
make_person("johan", "kessels")

