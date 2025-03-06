# Nested key-chain of people who have engaged in the poll of their 
# favorite number
poll_favorite = {
    "person_1": {
        "first": "anja",
        "last": "kessels",
        "fav_1": 30,
        "fav_2": 67,
    },
    "person_2": {
        "name": "koen",
        "last": "kessels",
        "fav_1": 94,
        "fav_2": 9,
    },
    "person_3": {
        "name": "johan",
        "last": "kessels",
        "fav_1": 8,
        "fav_2": 67,
    },
    "person_4": {
        "name": "luuk",
        "last": "kessels",
        "fav_1": 29,
        "fav_2": 23,
    },
    "person_5": {
        "name": "mike",
        "last": "rietjens",
        "fav_1": 77,
        "fav_2": 68,
    }
}

for user_name, favorite in poll_favorite.items():
    print("\nUsername" + user_name)
    full_name = user_name["name"] + " " + user_name["last"]
    favorite_num = favorite["fav_1"] + favorite["fav_2"]
    print(f"{full_name.title()}'s favorite number is {favorite_num}")