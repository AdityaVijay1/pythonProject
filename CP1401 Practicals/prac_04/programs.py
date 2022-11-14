# 1. Error Checking
"""

get worker_level

while worker_level<1 or worker_level>10

    display Invalid Worker Level

    get worker_level

total_salary=worker_level*5000

display With worker level worker_level, your salary is $total_salary"

"""
worker_level = int(input("Worker level: "))
while worker_level < 1 or worker_level > 10:
    print("Invalid worker level")
    worker_level = int(input("Worker level: "))
salary = worker_level * 5000
print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")
print()

# 2. Number Sequences

# a.
'''for i in range(1,101,2):
    display i'''
for i in range(1, 101, 2):
    print(i)
print()
# b.
'''for i in range(1896,2023,4):
    display i,end= ' ' '''
for i in range(1896, 2023, 4):
    print(i, end=' ')
print()
# c. Fibonacci Sequence
# This a sequence where the values of two numbers are combined and gives a third value and this goes on based on the user input
'''
First_Value=0
Second_Value=1
get Number_of_sequence_runs
display First_Value
display Second_Value
for i in range(Number_of_sequence_runs):
    Calculated_Value=First_Value+Second_Value
    display Calculated_Value
    First_Value=Second_Value
    Second_Value=Calculated_Value
'''
First_Value = 0
Second_Value = 1
Number_of_sequence_runs = int(input("Enter the number of times you want the sequence to go on till: "))
print(First_Value)
print(Second_Value)
for i in range(Number_of_sequence_runs - 2):
    Calculated_Value = First_Value + Second_Value
    print(Calculated_Value)
    First_Value = Second_Value
    Second_Value = Calculated_Value
print()

# 3. Menus
'''
display '(S)miley'
display '(F)rowny'
display '(Q)uit'
get UserInput.lower()
while True:
    if UserInput=='s':
        display ':)'
    elif UserInput=='f':
        display ':('
    elif UserInput=='q':
        display 'Farewell'
        break
    else:
        display 'Invalid choice'
    get UserInput.lower()
'''
print('(S)miley')
print('(F)rowny')
print('(Q)uit')
UserInput = input("Enter s for a smiley face, f for a frowny face or q to quit: ").lower()
while True:
    if UserInput == 's':
        print(':)')
    elif UserInput == 'f':
        print(':(')
    elif UserInput == 'q':
        print('Farewell')
        break
    else:
        print('Invalid choice')
    UserInput = input("Enter s for a smiley face, f for a frowny face or q to quit: ").lower()

print()

# 4. Accumulation
# Average Age
'''
SENTINEL = -1
total = 0
count = 0
get Age_Value
while Age_Value != SENTINEL:
    total = total + Age_Value
    count = count + 1
    get Age_Value
Average_Value = total / count
display Average_Value
'''
SENTINEL = -1
total = 0
count = 0
Age_Value = int(input("Enter the age: "))
while Age_Value != SENTINEL:
    total = total + Age_Value
    count = count + 1
    Age_Value = int(input("Enter the age: "))
Average_Value = total / count
print('Average Age:', Average_Value)
print()
# Smileys Count
'''
Count_S = 0
Count_F = 0
display '(S)miley'
display '(F)rowny'
display '(Q)uit'
get UserInput.lower()
while True:
    if UserInput == 's':
        display ':)'
        Count_S = Count_S + 1
    elif UserInput == 'f':
        display ':('
        Count_F = Count_F + 1
    elif UserInput == 'q':
        display 'Farewell'
        break
    else:
        display 'Invalid choice'
    get UserInput.lower()
display Count_S
display Count_F
'''
Count_S = 0
Count_F = 0
print('(S)miley')
print('(F)rowny')
print('(Q)uit')
UserInput = input("Enter s for a smiley face, f for a frowny face or q to quit: ").lower()
while True:
    if UserInput == 's':
        print(':)')
        Count_S = Count_S + 1
    elif UserInput == 'f':
        print(':(')
        Count_F = Count_F + 1
    elif UserInput == 'q':
        print('Farewell')
        break
    else:
        print('Invalid choice')
    UserInput = input("Enter s for a smiley face, f for a frowny face or q to quit: ").lower()
print("The number of smiley faces", Count_S)
print("The number of frowny faces", Count_F)
print()

# Total Numbers
'''
Total = 0
get Number_of_inputs
for i in range(1, Number_of_inputs + 1):
    Number = int(input(f"Enter number {i}: ", ))
    Total = Number + Total
display "The total of those", Number_of_inputs, "numbers is", Total
'''
Total = 0
Number_of_inputs = int(input("How many numbers do you want to add up? "))
for i in range(1, Number_of_inputs + 1):
    Number = int(input(f"Enter number {i}: ", ))
    Total = Number + Total
print("The total of those", Number_of_inputs, "numbers is", Total)
print()

# 5. Guessing Game
'''
SECRET=6
get guess
while guess != SECRET:
    display 'Guess again'
    Count=Count+1
    if guess>6:
        display Number is lower
    else:
        display Number is higher
    get guess
display "You got it",Count
'''
SECRET = 6
guess = int(input("Guess a number: "))
Count = 0
while guess != SECRET:
    print("Guess again!")
    Count = Count + 1
    if guess > 6:
        print("The number is lower")
    else:
        print("The number is higher")
    guess = int(input("Guess a number: "))
print("You got it in", Count, "!")

# 6. Nested Loops
'''
get Number_of_rows
get Number_of_columns
display Number_of_rows
display Number_of_columns
for i in range(Number_of_rows):
    for j in range(Number_of_columns):
        display j,end=' '
'''
Number_of_rows = int(input("Enter the number of rows:"))
Number_of_columns = int(input("Enter the number of columns:"))
print("Rows:", Number_of_rows)
print("Columns:", Number_of_columns)
for i in range(Number_of_rows):
    for j in range(Number_of_columns):
        print(j, end=' ')
    print()
print()
