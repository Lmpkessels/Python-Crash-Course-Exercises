# Creating a short variable so we can easily access the file, we want to access.
file_g_book = "/Users/luukkessels/Documents/Books - Python/guest_book.txt"


while True:
    name = input("Please, provide your name: ")
    print(f"Hello, {name.title()}!")

    with open(file_g_book, "a") as guest_book:
        guest_book.write(f"\n{name}")