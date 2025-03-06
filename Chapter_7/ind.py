### Excersise 7-10, Dream Vacation ###
# Dictionary for poll.
answers = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and respone.
    name = input("\nWhat is your name? ")
    answer = input("If you could visit one place in the world" 
                     " where would you go? ")

    # Store the response in the dictionary
    answers[name] = answer

    # Find out if anyone else is going to take the poll.
    repeat = input("Do you want to recommend someone else, who wants to" 
                   " take the poll? answer (yes/ no) ")
    if repeat == "no" or "No" or "NO":
        polling_active = False

# Polling is complete show the results
print("\n--- Poll Answers ---")
for name, question in answers.items():
    print(f"{name.title()} would like to visit {question.title()}")

    