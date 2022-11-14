"""Pseudocode
CP1401-Practical 8- Random Numbers

numbers = []
get random_number
get maximum
for i in range(random_number):
    random_value = random number
    numbers.append(random_value)
display numbers
display min(numbers)
display max(numbers)
display random.randint(0, maximum)
numbers.reverse()
display numbers
numbers.sort()
display numbers

"""

import random

numbers = []
random_number = int(input("How many random numbers: "))
maximum = int(input("Maximum Number: "))
for i in range(random_number):
    random_value = random.randint(0, maximum)
    numbers.append(random_value)
print("The numbers are: ", numbers)
print("The minimum is", min(numbers))
print("The maximum is", max(numbers))
print("A randomly chosen number is", random.randint(0, maximum))
numbers.reverse()
print("The numbers reversed are", numbers)
numbers.sort()
print("The numbers sorted are", numbers)
