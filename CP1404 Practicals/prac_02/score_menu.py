"""Pseudocode
"""
score=0
def main():
    MENU="(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit"
    choice=input(MENU)
    while choice != 'Q':
        if choice == 'G':
            score=get_score()
        elif choice == 'P':
            if score
            result=get_result(score)
        else:
            print("Invalid choice")
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


main()