def make_pizza(size, *toppings):
    """Summarize the pizza we're about to make."""
    print(f"\nMaking a {str(size)} -inch pizza with the following" 
          " toppings:")
    
    # Getting each topping in toppings and displaying it in list form.
    for topping in toppings:
        print(f"- {topping.title()}")


def make_person(name, last_name):
    """Summarizing person."""
    full_name = f"{name} {last_name}"
    print(f"\nScreaming {full_name.upper()} YOUR PIZZA IS READY!")