#A list that comunicates places I would like to visit in the future.
places_visit = ["Thailand", "Singapore", "Miami", "Dubai", "Monaco"]

#Here the list gets sorted by using the function; sorted.
print(sorted(places_visit))

#Here is the raw list.
print(places_visit)

#Here the list is sorted on alphabet, then reversed.
print(sorted(places_visit, reverse = True))

print(places_visit)

#Here i permanently change the order of the list
places_visit.reverse()
print(places_visit)

#Here the order is changed back to it's original state.
places_visit.reverse()
print(places_visit)

#Here the order gets put in alphabetic format.
places_visit.sort()
print(places_visit)

#Here the list gets ordered in alphabetic format first, then reversed.
places_visit.sort(reverse = True)
print(places_visit)