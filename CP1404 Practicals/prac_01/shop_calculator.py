"""
CP1404- Practical Week 1 shop_calculator.py

Pseudocode

TOTAL = 0
DISCOUNT = 0.1
get items
while items < 0:
    display "Invalid number of items entered"
    get items
for i in range(1,items+1):
    get price
    TOTAL = price + TOTAL
if TOTAL > 100:
    Discount_amount = TOTAL * DISCOUNT
    TOTAL = TOTAL - Discount_amount
display "Total price for {items} is ${TOTAL:.2f}"

"""
DISCOUNT_THRESHOLD=100
TOTAL = 0
DISCOUNT = 0.1
items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items entered")
    items = int(input("Number of items: "))
for i in range(1,items+1):
    price = float(input(f"Price of item {i}: "))
    TOTAL = price + TOTAL
if TOTAL > DISCOUNT_THRESHOLD:
    Discount_amount = TOTAL * DISCOUNT
    TOTAL = TOTAL - Discount_amount
print(f"Total price for {items} is ${TOTAL:.2f}")


