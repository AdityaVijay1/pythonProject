"""
CP1404 - Practical Week 1 broken_score.py
Broken program to determine score status

Pseudocode

get score
while score < 0 or score > 100:
    display "Invalid score"
    get score
else:
    if score >= 90:
        display "Excellent"
    elif score >= 50:
        display "Passable"
    else:
        display "Bad"

"""

score = float(input("Enter score: "))

while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))
else:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

