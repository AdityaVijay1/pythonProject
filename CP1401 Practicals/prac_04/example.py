"""

get birth_month

while birth_month < 1 or birth_month > 12

    display error message

    get birth_month



for count from 1 to birth_month

    display count

if birth_month >= half of 12

    display Second Half

else

    display First Half

"""

MINIMUM_MONTH = 1

MAXIMUM_MONTH = 12

MIDDLE_MONTH = MAXIMUM_MONTH / 2

birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))

while birth_month < MINIMUM_MONTH or birth_month > MAXIMUM_MONTH:
    print("Invalid month")

    birth_month = int(input("Enter your birth month: "))

for count in range(MINIMUM_MONTH, birth_month + MINIMUM_MONTH):
    print(count, end=" ")

if birth_month >= MIDDLE_MONTH:

    print("Second Half")

else:

    print("First Half")

print()
