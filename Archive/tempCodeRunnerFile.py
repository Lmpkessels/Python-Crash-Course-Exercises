# Poll for favorite restaurants.
prompt = input("What is your name? ")
prompt += input("What are your favorite restaurants, fill in max 3: ")

# Setting poll to active for while loop.
poll_active = True

# 
def get_favorite_restuarants(restaurant_1, restaurant_2, restaurant_3):
    """Getting data and summarizing data."""
    while get_favorite_restuarants():
        if restaurant_1:
            prompt = input(f"What are your favorite restaurants, fill in max 3: ")
            favorite_restaurant = (f"{restaurant_1}")
        elif restaurant_2:
            favorite_restaurant = (f"{restaurant_1}, {restaurant_2}")
        else:
            favorite_restaurant = (f"{restaurant_1}, {restaurant_2}," 
                                   f" {restaurant_3}")
        return favorite_restaurant.title()
    
    get_favorite_restuarants() == input(prompt)
    print(get_favorite_restuarants())