# Generate eache function you have learned in chapter 3 Lists...

# A list of great books
books = ["Law of Success", "Bible", "The Hypomanic Edge"]

# Sorting on alphabet and Turning the list around
books.sort(reverse = True)

print(books)

# Telling that every book is great
for book in books:
    print(f"The {book} is a great book!")


# Takes out the first book
books.pop(0)
print(books)

# Tells something about the bible
print(f"""\n\t
    The {books[0]} is a religious book that includes the old and new testatment
    """)

# Implementing three new books one at the beginning, middle, and end.
books.insert(0, "Ego is the Enemy")
books.insert(2, "Socrates")
books.append("Discourages")
print(books)

# Sorting new book list on alphabet
sorted(books, reverse = True)
print(books)

# Clearing book list
del books[0]
del books[1]
del books[2]
del books[-2]
del books[-1]

# Checking if book list is clear
print(len(books))