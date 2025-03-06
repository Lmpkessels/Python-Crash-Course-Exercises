# Declaring list with places I would like to visit
visit = ["Dubai", "Monaco", "America", "Thailand", "Singapore"]

# Showing list
print(visit)

# Ordering on alphabet without modifying the list
print(sorted(visit))

# Showing list is still in its original form
print(visit)

# Using sorted to print the list in reverse without changing the actual order
print(sorted(visit, reverse = True))

# Turning the order of the list around
visit.reverse()
print(visit)

# Changing it back to its original form
visit.reverse()
print(visit)

# Putting list in alphabetic order
visit.sort()
print(visit)

# List in alphabetic order first then reversed
visit.sort(reverse = True)
print(visit)