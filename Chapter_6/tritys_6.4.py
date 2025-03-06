### Excersis 6-4, Gloassary ###
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


### Excersise 6-5, Rivers ###
rivers = {
    "maas": "netherlands",
    "danuble": "germany",
    "seine": "france",
}

# Telling through what country each river runs
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

# Telling the name of each river
for river in rivers.keys():
    print(river.title())

# Telling each country the river runs throug
for country in rivers.values():
    print(country.title())


### Excersise 6-6, Polling ###
# A poll of people their favorite programming language
favorite_languages = {
    "luuk": "JavaScript",
    "peter": "Python",
    "frank": "HTML/CSS",
    "erik": "C",
    "elon": "C",
}

# List for poll people who have taken and are invited for the poll
list_poll = ["luuk", "erik", "johan", "koen", "anja", "elon"]

# Looping through the list, thanking the people who have taken the poll, 
# and invited people who haven't 
for people in list_poll:
    if people in favorite_languages:
        print(f"{people.title()}, Thank you for responding to the poll!")
    elif people not in favorite_languages:
        print(f"{people.title()}, You are invideted to take the poll!")

