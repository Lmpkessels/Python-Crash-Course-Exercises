### Returning a Simple Value ###
# Getting first name and last name, then creating a full name with it.
#
# # First_name and last_name, are called parameters.
def get_formatted_name(first_name, last_name):
    """Return a full name neatly formatted."""
    full_name = f"({first_name} {last_name})"
    return full_name.title()

# Here we get the given values and print the full name.
entrepreneur = get_formatted_name(first_name="naval", 
                                  last_name="ravikant")
print(entrepreneur)

# Function to get book, then we get its title and its author.
#
# Full_book is title + author.
#
# Title and author, are called parameters.
def get_book(title, author):
    """Description of a book"""
    full_book = f"({title} {author})"
    return full_book.title()

# Here we create a variable to store full book and show it to the user.
book = get_book(title="the milionaire fastland", author="Dj DeMarco")
print(book)


### Making an Argument Optional ###
# Getting full name but now also with middle name.
#
# Then creating a variable that stores the full name.
def get_formatted_name(first_name, middle_name, last_name):
    """Return a formatted full name."""
    full_name = f"({first_name} {middle_name} {last_name})"
    return full_name.title()

# Varible for who or what kind of person the name is assigned to in,
# this case a entrepreneur.
entrepreneur = get_formatted_name(first_name="john", middle_name="d", 
                                  last_name="rockefeller")
print(entrepreneur)


# Using a loop to get or, first, middle, and last. Or only first and last.
#
# We need to use if...else.... because otherwise it causes an error if 
# we have only first and last name, and first middle and last is optional.
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name neatly formatted."""
    if middle_name:
        full_name = (f"{first_name} {middle_name} {last_name}")
    else:
        full_name = (f"{first_name} {last_name}")
    return full_name.title()

# Creating variables that store the data of the given names.
author = get_formatted_name(first_name="viktor", middle_name="e", 
                            last_name="frankl")
investor = get_formatted_name(first_name="ray", last_name="dalio")

# Displaying full names.
print(author)
print(investor)


# Getting favorite restaurants with the 2nd and 3rth as optional.
def get_favorite_restaurant(rest_1="", rest_2="", rest_3=""):
    """Getting favorite restaurants"""
    if rest_3:
        full_restaurants = (f"{rest_1}, {rest_2}, {rest_3}")
    elif rest_2:
        full_restaurants = (f"{rest_1}, {rest_2}")
    else:
        full_restaurants = (f"{rest_1}")
    return full_restaurants.title()

# Assinging favorite restaurants to name.
luuks = get_favorite_restaurant(rest_1="rodeo", rest_2="hof van keent")
koens = get_favorite_restaurant(rest_1="bosmolenplas", rest_2="rodeo",
                                rest_3="hof van keent")
franks = get_favorite_restaurant(rest_1="schutterhoeve")

# Printing out all favorite restaurants of users.
print(luuks)
print(koens)
print(franks)


### Returning a dictionary ###
# defining a person in a dictionary.
def build_person(first_name, last_name):
    """Return a dictionary of first and last name about a person."""
    person = {"first": first_name, "last": last_name}
    return person
 
# Asigning values to full person.
full_person = build_person(first_name="luuk", last_name="kessels")

# Printing full person.
print(full_person)

# Gathering data of a person and storing it in a dictionary.
#
# Here we have added a optional parameter age="".
def build_person(first_name, last_name, age=""):
    """Return a dictionarry of information about a person."""
    person = {"first": first_name, "last": last_name, "age": age}
    if age:
        person["age"] = age
    return person

# Creating build person and assigning values to the parameters.
koen = build_person(first_name="koen", last_name="kessels", age=23)
luuk = build_person(first_name="luuk", last_name="kessels",)

# Displaying build persons.
print(koen)
print(luuk)


### Using a Function with a While Loop ###
# Creating formatted name.
def get_formatted_name(first_name, last_name):
    """Getting summarized full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# A while loop to get user data and provide the right name.
while True:
    print("\nPlease provide me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

   # Creating formatted name, then asking how he/she is doing today.
    formated_name = get_formatted_name(f_name, l_name)
    print(f"Hello {formated_name}!")
    break


# Getting favorite book
def get_favorite_book(name_book, author_book, release_book=""):
    """Summarizing favorite book"""
    favorite_book = f"{name_book.title()} {author_book.title()}" 
    f"{release_book}"
    return favorite_book

# Looping through question, and giving them the option to quit by 
# pressing 'q'.
while True:
    name = input("\nHello what is your name? ")
    print(f"Hello {name.title()} what is your favorite book?")

    # Getting name of book.
    n_book = input("Name book: ")
    if n_book == "q":
        break
    
    # Getting author of book.
    a_book = input("Author book: ")
    if a_book == "q":
        break
    
    # Getting release date of book.
    r_book = int(input("Realease book: "))
    if r_book == "q":
        break

    # Describing what person's favorite book is.
    persons_favorite_book = get_favorite_book(name_book=n_book, 
                            author_book=a_book, release_book=r_book)
    print(f"{name.title()}'s favorite book is {persons_favorite_book}.")

    # Asking if he/she has another favorite book, if no enter 'q' to,
    # leave the program.
    quit_ = input(f"{name.title()} do you want to provide another book?" 
                " If no enter 'q' to end the program. ")
    if quit_ == "q":
        break