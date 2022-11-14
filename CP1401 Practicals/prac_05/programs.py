# Input,process,output
# 1. Percentage program (I, P, O)

# get Original_Value,Change_Value
# Result=(Original_Value*Change_Value)+Original_Value
# display Original_Value,Change_Value,Result

Original_Value = float(input("Original: "))
Change_Value = float(input("Change: "))
Result = (Original_Value * Change_Value) + Original_Value
print(f"Original: {Original_Value}, Change: {Change_Value}, Result: {Result}")
print()

# Decision Structure
# 2. Time of day (Decision)

# get Time_Of_Day,Coming_Or_Going
# if Coming_Or_Going == 'going':
#     Reply = 'Bye'
# else:
#     Reply = 'Hi'
# if Time_Of_Day>=12:
#     TimePeriod='after'
# else:
#     TimePeriod='before'
# display TimePeriod,Coming_Or_Going,Reply


Time_Of_Day = int(input("Enter the time of the day: "))
Coming_Or_Going = input("Are you coming or going: ").lower()
if Coming_Or_Going == 'going':
    Reply = 'Bye'
else:
    Reply = 'Hi'
if Time_Of_Day >= 12:
    TimePeriod = 'after'
else:
    TimePeriod = 'before'
print(f"It is {TimePeriod} noon and you are {Coming_Or_Going}.{Reply}!")
print()

# 3. Coffee orders (Decision)

# EXTRA_COST_FOR_WHITE = 1
# BASIC_COST_S = 3
# BASIC_COST_M = 4
# BASIC_COST_L = 5
# get Coffee_Type.lower()
# get  Size.lower()
# if Size == 'small':
#     Cost = BASIC_COST_S
# elif Size == 'medium':
#     Cost = BASIC_COST_M
# else:
#     Cost = BASIC_COST_L
# if Coffee_Type != 'black':
#     Cost = Cost + EXTRA_COST_FOR_WHITE
# display Size,Coffee_Type,Cost

EXTRA_COST_FOR_WHITE = 1
BASIC_COST_S = 3
BASIC_COST_M = 4
BASIC_COST_L = 5
Coffee_Type = input("White or black coffee: ").lower()
Size = input("What cup size small, medium or large: ").lower()
if Size == 'small':
    Cost = BASIC_COST_S
elif Size == 'medium':
    Cost = BASIC_COST_M
else:
    Cost = BASIC_COST_L
if Coffee_Type != 'black':
    Cost = Cost + EXTRA_COST_FOR_WHITE
print(f"{Size.capitalize()} {Coffee_Type.capitalize()} Coffee: ${Cost}")
print()

# 4. Coffee orders with error-checking (Repetition)

# EXTRA_COST_FOR_WHITE = 1
# BASIC_COST_S = 3
# BASIC_COST_M = 4
# BASIC_COST_L = 5
#
# get Coffee_Type.lower()
# while Coffee_Type!='black' and Coffee_Type!='white':
#     print("Invalid Choice")
#     get Coffee_Type.lower()
# get Size.lower()
# while Size!='small' and Size!='medium' and Size!='large':
#     print("Invalid Choice")
#     get Size.lower()
# if Size == 'small':
#   Cost = BASIC_COST_S
# elif Size == 'medium':
#   Cost = BASIC_COST_M
# else:
#   Cost = BASIC_COST_L
# if Coffee_Type != 'black':
#   Cost = Cost + EXTRA_COST_FOR_WHITE
# display Size,Coffee_Type,Cost


EXTRA_COST_FOR_WHITE = 1
BASIC_COST_S = 3
BASIC_COST_M = 4
BASIC_COST_L = 5

Coffee_Type = input("White or black coffee: ").lower()
while Coffee_Type != 'black' and Coffee_Type != 'white':
    print("Invalid Choice")
    Coffee_Type = input("White or black coffee: ").lower()
Size = input("What cup size small, medium or large: ").lower()
while Size != 'small' and Size != 'medium' and Size != 'large':
    print("Invalid Choice")
    Size = input("What cup size small, medium or large: ").lower()
if Size == 'small':
    Cost = BASIC_COST_S
elif Size == 'medium':
    Cost = BASIC_COST_M
else:
    Cost = BASIC_COST_L
if Coffee_Type != 'black':
    Cost = Cost + EXTRA_COST_FOR_WHITE
print(f"{Size.capitalize()} {Coffee_Type.capitalize()} Coffee: ${Cost}")
print()


# 5. Accumulation (Repetition)

# get Low_Value
# get High_Value
# while True:
#     if Low_Value<High_Value:
#         break
#     else:
#         get Low_Value
#         get High_Value
# for i in range(Low_Value,High_Value+1):
#     display i,end=' '
#     Total=i+Total
# display Total

Total = 0
Low_Value = int(input("Low Value: "))
High_Value = int(input("High Value: "))
while High_Value <= Low_Value:
    print("Invalid value entered")
    High_Value = int(input("High Value: "))
for i in range(Low_Value, High_Value + 1):
    print(i, end=' ')
    Total = i + Total
print("totals:", Total)
print()