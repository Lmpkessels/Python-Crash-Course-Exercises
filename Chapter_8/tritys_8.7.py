### Excersise 8-8, User Albums ###
# A function that sumarizes the given values of the users favorite album.
def make_album(artis_name, album_title):
    """Summarizing discription of album"""
    album = {"artist": artis_name, "title": album_title}
    return album

# Asking name, to provide favorite album, and what to do if user wants 
# to quit program.
while True:
    name = input("\nHello user what is your name? ")
    print(f"{name.title()} please provide your favorite album:")
    print("Enter 'q' if you want to leave the program.")

    # Getting artist name. And adding if enter "q" quit.
    a_name = input("Artist name: ")
    if a_name == "q":
        break

    # Getting album name. And adding if enter "q" quit.
    a_title = input("Album title: ")
    if a_title == "q":
        break

    # Creating favorite album based on user input.
    favorite_album = make_album(artis_name=a_name, album_title=a_title)

    # Summarizing name and favorite album in one sentence to print message.
    print(f"{name}'s favorite album is; {favorite_album}")

    # Telling user what to do if they're done with the program.
    question_quit = input("Please enter 'q' if you want to quit the" 
                      " program. ")
    if question_quit == "q":
        break

# Thanking user for using program.
print(f"{name.title()} thanks for using the program!")
