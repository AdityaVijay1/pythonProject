import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1? A random integer number in between 5 and 20
# What was the smallest number you could have seen, what was the largest? 5 was the smallest and 20 was the largest
#
# What did you see on line 2? A random number between the start (inclusive) and stop value with a step value of 2
# What was the smallest number you could have seen, what was the largest? 3 is the smallest number and 9 is the largest number
# Could line 2 have produced a 4? No it couldn't have produced a 4.
#
# What did you see on line 3? A random float number in between 2.5(inclusive) and 5.5(not inclusive).
# What was the smallest number you could have seen, what was the largest? 2.5 is the smallest number and 5.499999999999999 is the largest number
#
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

print(random.randint(1,100))