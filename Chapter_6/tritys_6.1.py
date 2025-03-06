### Excersise 6-1, Person ###
# Information about a person I know stored in a dictionary
person = {
    "name": "Koen",
    "last_name": "Kessels",
    "date_of_birth": "09-04-2001",
    "age": 23,
}

# Printing out person name, lastname, date of birth, and age
print(person["name"])
print(person["last_name"])
print(person["date_of_birth"])
print(person["age"])

### Excersise 6-2, Favorite Numbers ###
# Storing people their favorite numbers in a dictionary
favorite_num = {
    "name1": "luuk", "favorite_number1": 29,
    "name2": "koen", "favorite_number2": 9,
    "name3": "johan", "favorite_number3": 8,
    "name4": "anja", "favorite_number4": 30,
    "name5": "peter", "favorite_number5": 88,
}

# Telling what everyone his favorite number is
print(favorite_num["name1"].title(), "and his favorite number is",
favorite_num["favorite_number1"])
print(favorite_num["name2"].title(), "and his favorite number is", 
favorite_num["favorite_number2"])
print(favorite_num["name3"].title(), "and his favorite number is",
favorite_num["favorite_number3"])
print(favorite_num["name4"].title(), "and her favorite number is",
favorite_num["favorite_number4"])
print(favorite_num["name5"].title(), "and his favorite number is",
favorite_num["favorite_number5"])

### Excersis 6-3, Gloassary ###
# Glossary for 5 words I have learned with its meaning
glossary = {
    "\nprint": "\na function for letting the program do its work",
    "\nfloat": "\nfloat can be used for assigning a floating point number",
    "\nint": "\nfunction int is used for a normal number",
    "\nstr": "\nfunction string is used for transforming a number to a string",
    "\ninput": "\nfunction input is used to ask the user for user input",
}

# Using a for loop to make it more efficient
for word, meaning in glossary.items():
    print(f"{word} means {meaning}")

