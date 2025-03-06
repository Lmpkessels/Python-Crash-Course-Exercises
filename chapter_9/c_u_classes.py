class Person():
    """Making an attend to illustrate a person."""
    def __init__(self, name, age):
        self.name = name.title()
        self.age = age
    
    def make_walk(self):
        """Making person walk."""
        print(f"{self.name} is walking.")

    def make_sit(self):
        """Making person sit down."""
        print(f"{self.name} is sitting.")

    def make_read(self):
        """Making person read."""
        print(f"{self.name} is reading.")


# Creating multiple different people.
#
# Creating person.
person_anja = Person(name="anja", age=57)
person_anja.make_read()

# Creating person.
person_johan = Person(name="johan", age=58)
person_johan.make_sit()

# Creating person.
person_koen = Person(name="koen", age=23)
person_koen.make_walk()

# Creating person.
person_luuk = Person(name="luuk", age=25)
person_luuk.make_sit()


# Writing name, and age about each individual.
print(f"{person_anja.name} is her name, and she is {person_anja.age} years " 
      "old.")

print(f"{person_johan.name} is his name, and he is {person_johan.age} years " 
      "old.")

print(f"{person_koen.name} is his name, and he is {person_koen.age} years "
      "old.")

print(f"{person_luuk.name} is his name, and he is {person_luuk.age} years " 
      "old.")