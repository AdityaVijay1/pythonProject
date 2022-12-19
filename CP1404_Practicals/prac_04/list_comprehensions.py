"""
CP1404/CP5632 Practical
List comprehensions
"""
import types

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for champions_name in names:
    first_initials.append(champions_name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [champions_name[0] for champions_name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# this splits each name and adds the first letters of each part to a string
full_initials = [champions_name.split()[0][0] + champions_name.split()[1][0] for champions_name in full_names]
print(full_initials)

# this example uses filtering to select only the names that start with A
a_names = [champions_name for champions_name in names if champions_name.startswith('A')]
print(a_names)

# and here's the join string method being used to create a single string from the names like:
# 'Ada Alan Angel Bob Jimi'
print(" ".join(sorted(names)))


print()
print()
# TODO: list comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [champions_name.lower() for champions_name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# TODO: list comprehension to create a list of integers from the above list of strings
numbers = [int(numbers) for numbers in almost_numbers]
print(numbers)

# TODO: list comprehension to create a list of only the numbers that are
# greater than 9 from the numbers (not strings) you just created
numbers_greater_than_9 = [number for number in numbers if number > 9]
print(numbers_greater_than_9)
# TODO: (more advanced) use a list comprehension and the join string method
# to create a string (not list) of the last names for those full names longer than 11 characters
# the result should be: 'Harlem, Hendrix, Lovelace'
full_names_longer_than_11_char= str([champions_name.split()[1] for champions_name in full_names if len(champions_name) > 11]).strip('[]')
print(full_names_longer_than_11_char)
