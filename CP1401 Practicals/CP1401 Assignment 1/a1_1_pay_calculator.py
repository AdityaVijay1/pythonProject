"""
CP1401 2022-2 Assignment 1
Program 1 – Pay Calculator
Student Name: Aditya Vijay
Date started: 25-08-2022


Pseudocode:

BASE_PAY=45
get Number_Of_Hours_Worked,Experience_Level
Extra_Pay=Experience_Level*5
display Experience_Level
Hourly_Pay_Rate = BASE_PAY + (BASE_PAY * (Extra_Pay / 100))
Total_Pay_Rate = Hourly_Pay_Rate * Number_Of_Hours_Worked
display Hourly_Pay_Rate
display Total_Pay_Rate

"""

BASE_PAY = 45
print("Experience Counts Pay Calculator")
Number_Of_Hours_Worked = int(input("Number of hours worked: "))
Experience_Level = int(input("Experience level: "))
Extra_Pay = Experience_Level * 5
print(f"Based on your experience level ({Experience_Level}): ")
# Calculating the hourly pay rate based on the extra pay
Hourly_Pay_Rate = BASE_PAY + (BASE_PAY * (Extra_Pay / 100))
# Calculating the total pay rate
Total_Pay_Rate = Hourly_Pay_Rate * Number_Of_Hours_Worked
Hourly_Pay_Rate = "{:.2f}".format(Hourly_Pay_Rate)
print(f"Your hourly pay rate is ${Hourly_Pay_Rate}")
Total_Pay_Rate = "{:.2f}".format(Total_Pay_Rate)
print(f"Your total pay is ${Total_Pay_Rate}")
