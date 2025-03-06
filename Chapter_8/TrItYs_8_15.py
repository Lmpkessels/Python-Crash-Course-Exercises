### Excersise 8-15, Printing Models ###
def customer_data(first_name, last_name, **about):
    """Summarizing customer data."""
    customer = {}
    customer["First name:"] = first_name
    customer["Last name:"] = last_name

    # Creating a key and value for about and slicing it to customer.
    for key, value in about.items():
        customer[key] = value
    return customer


def store(store_name, location, products_it_sells):
    """Summarizing store."""
    full = (f"Store name: {store_name}, Location: {location},"
    f" Products it sells: {products_it_sells}.")
    print(full.title())