"""
CP1401 2022-2 Assignment 1
Program 2 – Space Cadet Results
Student Name: Aditya Vijay
Date started: 25-08-2022

Pseudocode:

AVG_SCORE = 50
HONOUR_ROLL_SCORE = 90
get Practical_Score,Exam_Score
Total_Score=Practical_Score+Exam_Score
display Total_Score
if Total_Score < AVG_SCORE:
    display "You failed. Please try again next year."
elif Practical_Score >= Exam_Score:
    display "You will become a field agent."
else:
    display "You will become a desk officer."
if Total_Score >= HONOUR_ROLL_SCORE:
    display "Congratulations on making the honour roll!"

"""

AVG_SCORE = 50
HONOUR_ROLL_SCORE = 90
print("Welcome Trainee Space Cadet. How did you do?")
Practical_Score = int(input("Practical score (0-50): "))
Exam_Score = int(input("Exam score (0-50): "))
Total_Score = Practical_Score + Exam_Score
print(f"Your total score is {Total_Score} out of 100")
if Total_Score < AVG_SCORE:
    print("You failed. Please try again next year.")
elif Practical_Score >= Exam_Score:
    print("You will become a field agent.")
else:
    print("You will become a desk officer.")
if Total_Score >= HONOUR_ROLL_SCORE:
    print("Congratulations on making the honour roll!")
