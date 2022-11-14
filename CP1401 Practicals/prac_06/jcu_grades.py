"""3. JCU Grades

import random


function main():
    Score = get_Score()
    while True:
        if Score > 0:
            Grade = get_Grade(Score)
            display "The score {Score} is {Grade}"
            Score = get_Score()
        else:
            break

    get Number

    for i in range(Number):
        RandomScore = get_Random_Score()
        Grade = get_Grade(RandomScore)
        display "{RandomScore}:{Grade}"


function get_Score():
    get Score
    return Score


function get_Grade(Score):
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


function get_Random_Score():
    RandomScore = random.uniform(0, 100)
    RandomScore = "{:.1f}".format(RandomScore)
    RandomScore = float(RandomScore)
    return RandomScore


main()



"""
import random


def main():
    Score = get_Score()
    while True:
        if Score > 0:
            Grade = get_Grade(Score)
            print(f"The score {Score} is {Grade}")
            Score = get_Score()
        else:
            break

    Number = int(input("How many random scores: "))

    for i in range(Number):
        RandomScore = get_Random_Score()
        Grade = get_Grade(RandomScore)
        print(f"{RandomScore}:{Grade}")


def get_Score():
    Score = float(input("Score: "))
    return Score


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


def get_Random_Score():
    RandomScore = random.uniform(0, 100)
    RandomScore = "{:.1f}".format(RandomScore)
    RandomScore = float(RandomScore)
    return RandomScore


main()
