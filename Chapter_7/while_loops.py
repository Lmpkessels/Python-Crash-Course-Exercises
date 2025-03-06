# Looping till number 5 with a while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 #   If you do not put += 1 here the loop keeps 
                        #   going untill you close or stop the program


# A program that repeats the input till user wants to quit
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

# Repeating the message to user
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)


# Another program that keeps running till input is met to be false
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

# Checking what input is but here we use a flag to end the loop, the 
# message quit will make active false then the loop stops because a loop
# runs till a value is met to be false
active = True
while active == True:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


# Asking for a city the user wants to visit
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

# We keep asking till quit is filled in then we use break to end the loop
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


# 
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)

    