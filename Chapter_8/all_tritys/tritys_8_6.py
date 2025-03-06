### Excersise 8-1, Message ###
#
# Engaging with the user.
learning_about = input("What are you learning about? ")

# Parentheses doesn't need to be filled with a parameter.
def display_message():
    """Telling everyone what I am learning in this chapter."""
    message = f"I am learning about {learning_about}!"
    print(message.title())

# Calling function.
display_message()


### Excersise 8-2, Favorite Book ###
#
# Engaging with the user.
title = input("What is your favorite book? ")

# Function about favorite book.
def favorite_book(title):
    """Giving the title of my favorite book."""
    msg = f"One of his/her favorite books is, {title.title()}."
    print(msg)

# Calling function.
favorite_book(title)