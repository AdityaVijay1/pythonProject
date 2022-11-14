"""Pseudocode
CP1401-Practical 8- Test Scores

function main():
    scores=[]
    loop_count=5
    j=0
    for i in range(1,loop_count):
        score=get_valid_Score(i)
        scores.append(score)
    for i in scores:
        grade=get_Grade(i)
        j=j+1
        display "Score {j} was {i},which is {grade}"

    average_score=(sum(scores)/len(scores))
    display average_score
    if scores[-1]>average_score:
        display "The trend is positive"
    else:
        display "The trend is not positive"

def get_Grade(Score):
    if Score < 50:
        Grade = 'F'
    elif Score < 65:
        Grade = 'P'
    elif Score < 75:
        Grade = 'C'
    elif Score < 85:
        Grade = 'D'
    else:
        Grade = 'HD'
    return Grade
def get_valid_Score(i):
    get Score
    while Score<0 or Score>100:
        print('Invalid choice')
        get Score
    return Score
main()
"""


def main():
    scores = []
    loop_count = 5
    j = 0
    for i in range(1, loop_count):
        score = get_valid_Score(i)
        scores.append(score)
    for i in scores:
        grade = get_Grade(i)
        j = j + 1
        print(f"Score {j} was {i},which is {grade}")

    average_score = (sum(scores) / len(scores))
    print("The average score was", average_score)
    if scores[-1] > average_score:
        print("The trend is positive")
    else:
        print("The trend is not positive")


def get_Grade(Score):
    if Score < 50:
        Grade = 'F'
    elif Score < 65:
        Grade = 'P'
    elif Score < 75:
        Grade = 'C'
    elif Score < 85:
        Grade = 'D'
    else:
        Grade = 'HD'
    return Grade


def get_valid_Score(i):
    Score = float(input(f"Score {i}: "))
    while Score < 0 or Score > 100:
        print('Invalid choice')
        Score = float(input(f"Score {i}: "))
    return Score


main()
