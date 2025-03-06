def city_country(city_name, country):
    """Summarizing city nama and country into one sentence"""
    summary = (f"{city_name.title()}, {country.title()}")
    return summary

# Here we call 3 functions, we do this by creating a variable then,
# asigning the function to it with the parameters inside the paratheses. 
get_city_country_1 = city_country(city_name="stramproy", 
country="the netherlands")

get_city_country_2 = city_country(city_name="dubai", 
country="united arab emirates")

get_city_country_3 = city_country(city_name="miami", country="amerika")

# Getting city and country on terminal.
print(f"Here follows a city and it's country: {get_city_country_1}")
print(f"Here follows a city and it's country: {get_city_country_2}")
print(f"Here follows a city and it's country: {get_city_country_3}")


# Function that makes a summary of a music album including artist name, 
# album title, and number of tracks.
def music_album(artist_name, album_title, number_o_tracks=""):
    """Summarizing a music album in a dictionary."""
    full_album = {"Artist": artist_name.title(), 
    "Album title": album_title.title(), 
    "Number of Tracks": number_o_tracks}
    return full_album

# Creating full album with name and title.
album_summary_0 = music_album(artist_name="eminem", 
album_title="relapse")
album_summary_1 = music_album(artist_name="50 cent", 
album_title="get rich or die tryin")
album_summary_2 = music_album(artist_name="the infamous", 
album_title="mob deep", number_o_tracks=16)

# Getting three dictionaries on terminal.
print(album_summary_0)
print(album_summary_1)
print(album_summary_2)


# Program to get user information about their favorite music album.
def music_album(artist_name, album_title, number_o_tracks=""):
    """Summarizing a music album in a dictionary."""
    full_album = {"Artist": artist_name.title(), 
    "Album title": album_title.title(), 
    "Number of Tracks": number_o_tracks}
    return full_album
    
while True:
    name = input("\nProvide me your name: ")
    print(f"\n{name.title()} could you please provide me your favorite album:"
    "\nEnter 'q' when done with program.\n")

    # Asking user for artist name.
    a_name = input("Artist name: ")
    if a_name == "q":
        break

    # Asking user for album title.
    a_title = input("Album title: ")
    if a_title == "q":
        break

    # Asking user for number of tracks.
    n_o_tracks = input("Number of Tracks: ")
    if n_o_tracks == "q":
        break

    # Asking user to quit program when done.
    quit_program = input("\nWhen done please enter 'q' if to quit" 
    " the program: ")
    if quit_program == "q":
        break
    
# Creating full album based on user input.
full_album = music_album(artist_name=a_name, album_title=a_title,
number_o_tracks=n_o_tracks)

# Displaying full album.
print(f"\n{name.title()}'s favorite album in summary is {full_album}")