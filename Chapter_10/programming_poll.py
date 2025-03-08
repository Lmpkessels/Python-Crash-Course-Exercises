# Creating a variable for poll file, so we have easy acccess.
poll_file = "/Users/luukkessels/Documents/Books - Python/programming_poll.txt"

while True:
    name = input("Please provide me your name: ")
    question = input(f"{name.title()}, tell me why do you like programming? ")
    summary = (f"{name.title()}, likes programming because, {question}")

    with open(poll_file, "a") as programming_poll:
        programming_poll.write(summary)