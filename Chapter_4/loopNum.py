# Creating an empty list to store numbers from 1 to 1.000.000
numbers = []
# A loop to print each number in range from 1 -- 1.000.000
for number in range(1, 1000001):
    # Here a append the number loop, to the numbers list.
    numbers.append(number)

# Showing the list from 1 to 1.000.000
print(numbers)
# Showing min number which = 1
print(min(numbers))
# Showing max number which = 1.000.000
print(max(numbers))
# Giving the total of each number with sum()
print(sum(numbers))

# An list of odd numbers range 1 - 20
odd_numbers = []
# Looping through the list an printing the numbers
for odd_number in range(1, 20, 2):
    # Appending the for loop to the odd_numbers list
    odd_numbers.append(odd_number)

# Showing all odd numbers in range 1 - 20 to the user
print(odd_numbers)

# Multiplying numbers from range 3 to 30 by 3
list_multiples = []
# Creating the multiples 3 to 30
for multiples in range(3, 30, 3):
    # Appending the numbers to the list
    list_multiples.append(multiples)
# Showing each number from range 3 - 30
print(list_multiples)

# Declaring an empty list
cube_numbers_1 = []

# Creating a for loop with range 1 - 11
for num in range(1, 11):
    # Creating a cube for every number ranging from 1 - 10
    numbers = num**3
    # Appending numbers to cube_numbers_1 list
    cube_numbers_1.append(numbers)
# Showing each cube number
print(cube_numbers_1)

# Each cube number from range 1 - 10
cube_numbers = [num**3 for num in range(1, 11)]
# Showing each cube number from range 1 - 10
print(cube_numbers)