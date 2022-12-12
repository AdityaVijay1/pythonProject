"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.


CP1404- Practical Week 1 sales_bonus.py

Pseudocode

ONUS_BELOW_1000 = 0.1
BONUS_ABOVE_1000 = 0.15
get sales
while sales > 0.0:
    if sales < 1000:
        bonus = int(sales * BONUS_BELOW_1000)
    else:
        bonus = int(sales * BONUS_ABOVE_1000)
    display bonus

"""

BONUS_BELOW_1000 = 0.1
BONUS_ABOVE_1000 = 0.15
sales = float(input("Enter sales: $"))
while sales > 0.0:
    if sales < 1000:
        bonus = int(sales * BONUS_BELOW_1000)
    else:
        bonus = int(sales * BONUS_ABOVE_1000)
    print("Bonus:", bonus)
