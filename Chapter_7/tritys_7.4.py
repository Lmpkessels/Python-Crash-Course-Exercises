# Asking user for toppings they would like to add to their pizza
prompt = ("\nHello user, please enter the toppings you'd like on your"
" pizza: ")
prompt += "\nWhen provided all toppings enter 'quit' "

# Telling the user were adding the provided topping to the pizza
while True:
    topping = input(prompt)

    # Here we tell the program what to do - put out sentence adding 
    # topping or quit program
    if topping.strip() == 'quit':
        break
    else:
        print(f"We're adding {topping} to your pizza!")


# Checking age of visitor for movie
# 
# If you want to expend a line and follow PEP 8 guidlines you should use
# parentheses to write your string in then the program knows its a whole  
prompt_age = ("\nPlease provide me your age so we can evaluate the price" 
" you need to pay for your ticket: ")
prompt_age += "\nType '0' to finish the program. "

while True:
    movie_tickets = int(input(prompt_age))

    # Telling visitor what the price is for the movie based on their 
    # input
    if movie_tickets == 0:
        break
    elif movie_tickets < 3:
        print("Your entry is Free!")
    elif movie_tickets < 12:
        print("Your entry ticket costs $10,-")
    else:
        print("Your entry ticket costs $15,-")


# As chatGPT told this works but does not allow repeated inputs
# Asking user to provide age
prompt_age = ("\nPlease provide me your age so we can evaluate the" 
" price of your ticket: ")

# Telling program where to get its data from
age = int(input(prompt_age))

# Using an if else statement to provide the right message for the user
if age < 3:
    print("Tickets for toddlers under 3 are Free!")
elif age < 12:
    print("Tickets for kids between 3 and 12 years young are $10,- ")
else:
    print("Tickets for over 12 years are $15,- ")


# Asking user for data input so we can provide a pizza with the toppings
# they wish for
prompt_2 = ("\nPlease provide me the toppings you would like to have" 
" on your pizza thank you: ")
prompt_2 += ("\nWhen your done enter 'quit' then we'll go to work! ")

# Checking status of their toppings
active = True
while active:
    pizza = input(prompt_2)

    if pizza == 'quit':
        active = False
    else:
        print(f"Were adding {pizza} to your pizza!")


