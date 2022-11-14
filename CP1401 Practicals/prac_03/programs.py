# 1. Tax


# Algorithm

# display Python Party Tax Program - Where Tax is a Party
# get Income
# if Income<100:
# total_tax=0
# elif Income<1000
#     total_tax=Income*0.05
# else:
#     total_tax=Income*0.1
# take_home_pay=Income-total_tax
#
# display total_tax
# display  take_home_pay,


TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))
if income < TAX_THRESHOLD_LOW:
    total_tax = 0
elif income < TAX_THRESHOLD_HIGH:
    total_tax = income * 0.05
else:
    total_tax = income * 0.1
take_home_pay = income - total_tax
print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")

# With Changes including $500
TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000
TAX_THRESHOLD_MID = 500
print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))
if income < TAX_THRESHOLD_LOW:
    total_tax = 0
elif income < TAX_THRESHOLD_MID:
    total_tax = income * 0.02
elif income < TAX_THRESHOLD_HIGH:
    total_tax = income * 0.05
else:
    total_tax = income * 0.1
take_home_pay = income - total_tax
print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")

# 2.Car Insurance
''' Algorithm
get Age
if Age<18:
    display Hire refused
elif Age<25:
    display Insurance required
else:
    display Insurance not required
'''

UNDER_18 = 18
UNDER_25 = 25
Applicant_Age = int(input("Enter your age:"))
if Applicant_Age < UNDER_18:
    print("Hire refused")
elif Applicant_Age >= UNDER_18 and Applicant_Age < UNDER_25:
    print("Insurance required")
else:
    print("Insurance not required")

# 3. Simple Password Checker
'''Algorithm
get Password
if Password==SECRET_PASSWORD:
  display Access granted
else:
  display Access denied'''

SECRET_PASSWORD = '123apples'
Password = input("Enter the password:")
if Password == SECRET_PASSWORD:
    print("Access granted")
else:
    print("Access denied")

# 4. Dog Years
'''Algorithm
get Age
if Age<=2:
    Dog_years=Age*10.5
else:
    Dog_years= 21+(Age-2)*4
display Dog_years'''

LOW_AGE = 2

FIRST_YEAR_DOG_HUMAN = 10.5

FIRST_TWO_CONVERTED_DOG_AGE = 21

AFTER_SECOND_YEAR_DOG_HUMAN = 4

age = float(input("Input dog's age in human years here: "))

if age <= LOW_AGE:

    dog_year = age * FIRST_YEAR_DOG_HUMAN

else:

    dog_year = (age - LOW_AGE) * AFTER_SECOND_YEAR_DOG_HUMAN + FIRST_TWO_CONVERTED_DOG_AGE

print(dog_year)

# 5. Rock of Ages
'''Algorithm
get Age
if Age<0 or Age>120: 
   display Invalid Age
elif Age<18
   display Teen
elif Age<25
    display Young Adult
elif Age<50
    display Adult
else:
    display Senior Citizen
'''

Age = int(input("Enter your Age:"))
if Age <= 0 or Age >= 120:
    print("Invalid Age")
elif Age < 13:
    print("Young Teen")
elif Age < 18:
    print("Teen")
elif Age < 25:
    print("Young adult")
elif Age < 50:
    print("Adult")
else:
    print("Senior Citizen")

# 6.Speeding Fines
'''Algorithm
get speed,speed_limit
speed_difference=speed-speed_limit
if speed_difference<13:
    display $177,demerit points=1
elif speed_difference<20:
    display $266,demerit points=3
elif speed_difference<30:
    display $444,demerit points=4
elif speed_difference<40:
    display $622,demerit points=6
else:
    display $1245,demerit points=8
'''
Speed = int(input("Enter the speed:"))
Speed_Limit = int(input("Enter the speed limit:"))
Speed_difference = Speed - Speed_Limit
if Speed_difference < 13:
    print("$177 fine")
elif Speed_difference < 20:
    print("$266 fine")
elif Speed_difference < 30:
    print("$444 fine")
elif Speed_difference < 40:
    print("$622 fine")
else:
    print("$1,245 fine")
