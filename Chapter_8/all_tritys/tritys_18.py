def make_person(first_name, last_name, **about):
    """Description of user."""
    person = {}
    person["first_name:"] = first_name.title()
    person["last_name:"] = last_name.title()

    # Getting key-value for dictionary.
    for key, value in about.items():
        person[key] = value
    return person