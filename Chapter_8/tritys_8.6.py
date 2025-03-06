### Excersise 8-6, City Names ###
# Function for taking in city and country.
def city_country(city_name, country_city):
    """Summarizing city and it's country place."""
    summary = f"{city_name.title()} is in {country_city.title()}."
    return summary

# Giving three city's and the country where it's located.
print(city_country(city_name="weert", country_city="the netherlands"))
print(city_country(city_name="dubai", country_city="united arab" 
" emirates"))
print(city_country(city_name="monaco", country_city="monaco"))


### Excersise 8-7, Albums ###
# Function describing a music album.
def make_album(artist_name, album_title, number_of_tracks=""):
    """Describing a music album."""
    album = {"artist": artist_name.title(), "title": 
    album_title.title(), "numbers of tracks": number_of_tracks}
    return album

# Providing each album, with artist name, album title, and if given 
# number of tracks.
print(make_album(artist_name="mobb deep", album_title="the infamous", 
number_of_tracks=16))
print(make_album(artist_name="eminem", album_title="slim shady lp"))
print(make_album(artist_name="50 cent", album_title="get rich or die" 
" tryin", number_of_tracks=16))


### Excersise 8-8, User Albums ###
def make_album(artist_name, album_title, number_of_tracks=""):
    """Describing a music album."""
    album = {"Artist name": artist_name.title(), "Album title": album_title,
    "number_of_tracks": number_of_tracks}
    return album

# Asking user for their name, their favorite album, and what they 
# need to do if they want to leave the program.
while True:
    name = input("\nUser, what is your name? ")
    print(f"{name.title()} please provide me your favorite album:")
    print("If you want to leave the program enter 'q'.")

    # Getting artist name from user.
    a_name = input("Artist name: ")
    if a_name == "q":
        break

    # Getting album title from user.
    a_title = input("Album title: ")
    if a_title == "q":
        break
        
    # Getting number of track from user.
    n_o_tracks = int(input("Number of Tracks: "))
    if n_o_tracks == "q":
        break
    
    # Declaring person's favorite album based on user input.
    #
    # Then printing their favorite album, and asking if they are done,
    # to press 'q' so they leave the program.
    persons_fav_album = make_album(artist_name=a_name, 
                        album_title=a_title, 
                        number_of_tracks=n_o_tracks)
    print(f"{name.title()}'s favorite album {persons_fav_album}")
    

    # Telling user what to do if they're done with the program.
    quit_ = input(f"{name.title()} please enter 'q' if you want to leave the" 
              " program.")
    if quit_ == "q":
        break

print(f"{name} thank you for using the program!")