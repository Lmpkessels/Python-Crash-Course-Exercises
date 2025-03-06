### Excersise 8-6, City names ###

# Creating a function called city_country.
def city_country(city_name, country_located):
    """Summary of city name and country located."""
    city_and_country = f"\n{city_name}, {country_located}"
    print(city_and_country.title())

# Calling function and asigning values to parameter.
city_country(city_name="flevoland", country_located="the netherlands")


### Excersise 8-7, album ###

# Declaring a function called make_album.
def make_album(artist_name ,album_title, number_of_tracks=""):
    """Summarizing a album in a dictionary."""
    music_album = {}
    music_album["Artist name:"] = artist_name.title()
    music_album["Album title:"] = album_title.title()
    music_album["Number of Tracks:"] = number_of_tracks
    print(f"{music_album}")

# Calling function with values asigned to it's parameters.
#
# Displaying message - Favorite album is.
print("\nFavorite album is:")
make_album(artist_name="eminem", album_title="relapse")
make_album(artist_name="50 cent", album_title="get rich or die trying", 
           number_of_tracks=16)
make_album(artist_name="guns 'n' roses", album_title="apetite for destruction", 
           number_of_tracks="12")


### Excersise 8-8, User Albums ###
def make_album(artist_name, album_title, number_o_tracks=""):
    """
    Getting user input for favorite album.
    When received summarizing album.
    """
    album_summary = (f"{artist_name.title()} {album_title.title()} "
    f"{number_o_tracks}")
    return album_summary

# Using while loop for while true do following.
while True:

    # Telling user what program is, to enter her/his name, and what to do if 
    # done.
    print("\nHello and welcome to the favorite album poll.")  
    name = input("\nPlease enter your name: ")
    print(f"\nHello {name.title()} give us your favorite album:")
    print("(Enter 'q' any time you want to quit.)")

    # Getting favorite artist from user.
    a_name = input("Artist name: ")
    if a_name == 'q':
        break

    # Getting album title from user.
    a_title = input("Album title: ")
    if a_title == 'q':
        break

    # Getting number of tracks from user.
    n_o_tracks = input("Number of Tracks: ")
    if n_o_tracks == 'q':
        break

album = make_album(a_name, a_title, n_o_tracks)
print(f"{name.title()} his favorite album is {album}")