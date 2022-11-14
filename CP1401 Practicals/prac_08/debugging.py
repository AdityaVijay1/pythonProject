"""CP1401 - Practical 8 - Debugging."""

# Debug program 1 - friends' names
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(1, len(names)):
    print(f"{i}. {names[i]}")
last_number = len(names)
print(f"The last name (number {last_number}) is {names[last_number]}")
#
# Problem(s) for program 1:
# The for loop will not print the first element of the list as it starts from the 1st index and not the 0th index. Loop should also have i+1 to show the correct order of names in a sequence.
# last_number variable should be assigned the last value of the list but by assigning len we will get the index of a number not present in the list(Index error-out of range). Should be replaced with len(names)-1.


# Fixed code for program 1:
# names = ["Abby", "Jerome", "Olivia", "Monique"]
# print("My friends' names: ")
# for i in range(0, len(names)):
#     print(f"{i+1}. {names[i]}")
# last_number = len(names)-1
# print(f"The last name (number {last_number+1}) is {names[last_number]}")


# Debug program 2 - title-casing country names
countries = ("australia", "new zeaLAND", "India")
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)  # country names should be in title-case now

# Problem(s) for program 2:
# countries variable should be a list not a tuple because we need to modify it and is not possible in a tuple

# Fixed code for program 2:
# countries = ["australia", "new zeaLAND", "India"]
# for i in range(len(countries)):
#     countries[i] = countries[i].title()
# print(countries)
