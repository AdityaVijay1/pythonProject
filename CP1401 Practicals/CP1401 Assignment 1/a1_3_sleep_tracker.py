"""
CP1401 2022-2 Assignment 1
Program 3 – Sleep Tracker
Student Name: Aditya Vijay
Date started: 25-08-2022


Pseudocode:

REQUIRED_SLEEP = 40
NO_SLEEP = 0
MAXIMUM_SLEEP = 24
display "Sleep Tracker"
Total_Sleep = 0
for i in range(1, 6):
    get Sleep_Hours
    while Sleep_Hours < NO_SLEEP or Sleep_Hours > MAXIMUM_SLEEP:
        display "Invalid number of hours."
        get Sleep_Hours
    Total_Sleep = Total_Sleep + Sleep_Hours
Sleep_Debt = REQUIRED_SLEEP - Total_Sleep
print "Recommended total sleep is:,REQUIRED_SLEEP"
print "Your total hours of sleep :,Total_Sleep"
display "Your sleep debt over this time is:,Sleep_Debt"

"""

REQUIRED_SLEEP = 40
NO_SLEEP = 0
MAXIMUM_SLEEP = 24
print("Sleep Tracker")
Total_Sleep = 0
for i in range(1, 6):
    Sleep_Hours = float(input(f"Night {i} hours of sleep: "))
    # Error Checking for any invalid values entered for sleep hours
    while Sleep_Hours < NO_SLEEP or Sleep_Hours > MAXIMUM_SLEEP:
        print("Invalid number of hours.")
        Sleep_Hours = float(input(f"Night {i} hours of sleep: "))
    Total_Sleep = Total_Sleep + Sleep_Hours
# Calculating the sleep debt
Sleep_Debt = REQUIRED_SLEEP - Total_Sleep
print(f"Recommended total sleep is: {REQUIRED_SLEEP}")
print(f"Your total hours of sleep : {Total_Sleep}")
if Total_Sleep >= REQUIRED_SLEEP:
    print("You are getting enough sleep. Keep it up!")
else:
    print(f"Your sleep debt over this time is: {Sleep_Debt}")
