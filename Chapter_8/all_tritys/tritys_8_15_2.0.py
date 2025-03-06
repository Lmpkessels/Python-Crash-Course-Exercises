# Using 3 different imports to import a function from another file.
#
# Import as p here we creat a shorcut to have clear and fast code.
import tritys_8_15 as p 

# Here we create the function and asign values to the parameters.
p.user_profile(user_name="luuk", user_last_name="kessels", 
               e_mail="lmpkessels@gmail.com")


# Here we import user_profile out of document.
from tritys_8_15 import user_profile

# Creating user profile, asigning values to parameters.
user_profile(user_name="luuk", user_last_name="kessels", 
               e_mail="lmpkessels@gmail.com")


# Here we import user_profile from document tr, then we make a shortcut called 
# up, so we can call it fast.
from tritys_8_15 import user_profile as up

# Creating user profile, asigning values to parameters.
up(user_name="luuk", user_last_name="kessels", e_mail="lmpkessels@gmail.com")

