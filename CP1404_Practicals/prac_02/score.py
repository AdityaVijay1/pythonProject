"""
CP1404 - Practical Week 2 score.py
Broken program to determine score status

Pseudocode

function main():
    score = get_score()
    result = get_result(score)
    display result


function get_score():
    get score

    while score < 0 or score > 100:
        display "Invalid score"
        get score
    return score


function get_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

"""


def main():
    score = get_score()
    result = get_result(score)
    print(result)


def get_score():
    score = float(input("Enter score: "))

    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: " ))
    return score


def get_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
