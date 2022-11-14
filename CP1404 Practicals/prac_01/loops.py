"""
CP1404- Practical Week 1 loops.py

Pseudocode

for i in range(1, 21, 2):
    display i, end=' '


# a
for i in range(0, 101, 10):
    display i, end=' '


# b
for i in range(20, 0, -1):
    display i, end=' '


# c
get stars
for i in range(stars):
    display '*', end=' '

# d
get stars
for i in range(stars+1):
    for j in range(i):
        display '*', end=' '


"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
stars = int(input("Number of stars: "))
for i in range(stars):
    print('*', end=' ')
print()
print()
# d
stars = int(input("Number of stars: "))
for i in range(stars + 1):
    for j in range(i):
        print('*', end=' ')
    print()
print()
