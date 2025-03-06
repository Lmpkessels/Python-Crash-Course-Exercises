### Looping throught all key value pairs ###
user_0 = {
    "username": "Lmp_kessels",
    "last": "luuk",
    "first": "kessels",
}

## For looping through a key you create two values
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


# List of people their name and their favorite programming languages
#
# "luuk": is the key, and "JavaScript" is the chain, together is creates 
# a key chain
favorite_languages = {
    "luuk": "JavaScript",
    "peter": "Python",
    "frank": "HTML/CSS",
    "erik": "C",
    "elon": "C",
}

# Telling everyone's favorite language
#
# Always use .items() to get the items out of the list
for name, language in favorite_languages.items():
    print(name.title() + "'s", "favorite language is " + language + ".")

# Seeing who has taken place in the poll
#
# We use the keys() method to get only the keys out of the key-chain
for name in favorite_languages.keys():
    print(name.title())

# A list of my friends
friends = ["frank", "erik"]
for name in favorite_languages:
    print(name.title())

# Telling program what to do if name is in friends
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is "
        + favorite_languages[name].title())

# Telling person who is not in poll what to do
if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Here we use the sorted function to get our keys in alphabetic ordeer 
#
# This code thanks the people who engaged in the poll
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# A message for the mentioned languages
#
# We wrap set() around favorite_languages so we don't get duplicates
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

### NoTe: Don't forget to look at the error that is given out in the 
# terminal you can learn a lot from it! ###