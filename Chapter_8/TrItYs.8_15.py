# Importing function, and assigning it as alias T.
import TrItYs_8_15 as t

# Creating variable which calls the function with the data of customer. 
#
# And calling function.
customer = t.customer_data("luuk", "kessels", 
                           location_born="houtbroek 2a 6039RL stramproy", 
                           date_born="23-02-2000")
print(customer)


# Doing exactly the same but in a different way.
from TrItYs_8_15 import customer_data as cd

# Calling function
customer = cd("luuk", "kessels", age="25", born="23-02-2000")
print(customer)


# Importing file which we asign to alias p because we're going to create a prada
# store list.
import TrItYs_8_15 as p

# Creating a list which summarizes a prada store.
p.store(store_name="prada", 
        location="pieter cornelisz hooftstraat 63H amsterdam", 
        products_it_sells="fashion")


# Doing exactly the same, but different.
from TrItYs_8_15 import store as p

# Calling function, and assigning values to it.
p(store_name="new tailor", location="minrebroederstraat 27, 3512 GS utrecht", 
  products_it_sells="custom made clothing")


# Again doing exactly the same but different.
import TrItYs_8_15

# Calling function and asigning values to parameters.
TrItYs_8_15.store(store_name="amac", location="demer 16, 5611 AR eindhoven", 
                  products_it_sells="hardware")

