# Importing file that includes a function. And asigning it to a short alias
# called mp.
import tritys_18 as mp

# Creating person.
person = mp.make_person(first_name="luuk", last_name="kessels", age=25, 
            birt_date="23-02-2000")

# Displaying person.
print(person)


# Import only file.
import tritys_18

# Creating person by calling function.
person = tritys_18.make_person(first_name="anja", last_name="kessels", age="57", 
                               birth_date="30-08-1967")

# Displaying person.
print(person)


# Importing function from file, and giving it a short alias named; koen.
from tritys_18 import make_person as koen

# Creating person.
person_koen = koen(first_name="koen", last_name="kessels", age="23", 
              birth_date="09-04-2001")

# Displaying person
print(person_koen)


# Importing file, then asigning alias name johan to it.
import tritys_18 as johan

# Here we creat person johan.
person_johan = johan.make_person(first_name="johan", last_name="kessels", 
                                 age=58, birth_date="08-01-1967")

# Here we call person johan.
print(person_johan)