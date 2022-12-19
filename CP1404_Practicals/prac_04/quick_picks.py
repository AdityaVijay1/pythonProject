import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
numbers = []
quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    current_numbers = []
    for j in range(0,6):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in current_numbers:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        current_numbers.append(number)
    numbers.append(current_numbers)
    # Another method
    # for i in current_numbers.sort():
    #     print(f"{i:>2}", end=' ')
    # print()

for i in numbers:
    i.sort()
    for j in i:
        print(f"{j:>2}",end= ' ')
    print()


