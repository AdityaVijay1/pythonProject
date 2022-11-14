"""Pseudocode
"""


def main():
    score = 0
    MENU = "(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit: "
    choice = input(MENU)
    while choice != 'Q':
        if choice == 'G':
            score = get_score()
        elif choice == 'P':
            if score == 0:
                score = get_score()
            result = get_result(score)
            print(result)
        elif choice == 'S':
            if score == 0:
                score = get_score()
            display_stars(score)
        else:
            print("Invalid choice")
        choice = input(MENU)
    print("Farewell")


def get_score():
    score = float(input("Enter score: "))

    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def get_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def display_stars(score):
    for i in range(int(score)):
        print('*', end='')
    print()


main()
