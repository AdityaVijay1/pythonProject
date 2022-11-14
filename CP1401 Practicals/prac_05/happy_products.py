 # Happy Products (All Together Now)

# while True:
#     display "Menu:"
#     display "(I)nstructions"
#     display "(C)alculate"
#     display "(Q)uit"
#     get Choice.upper()
#     if Choice != 'Q' or Choice != 'C' or Choice != 'I':
#         display "Invalid Choice"
#     elif Choice == 'I':
#         display "Enter the number of products you want to buy and your chosen price."
#         display "If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!"
#     elif Choice == 'C':
#         while True:
#             get Number_Of_Products
#             if Number_Of_Products < 0:
#                 display "Invalid Input"
#             else:
#                 break
#         while True:
#             get Price
#             if Price < 0:
#                 display "Invalid Input"
#             else:
#                 break
#         Total_Price = Number_Of_Products * Price
#         print(f"{Number_Of_Products} x {Price} products = ${Total_Price: 2f }")
#     else:
#         display "Farewell"
#         break


while True:
    print("Menu:  ")
    print("(I)nstructions ")
    print("(C)alculate ")
    print("(Q)uit ")
    Choice = input("Choice: ").upper()
    if Choice == 'I':
        print("Enter the number of products you want to buy and your chosen price.")
        print("If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
    elif Choice == 'C':
        while True:
            Number_Of_Products = int(input("Number of products: "))
            if Number_Of_Products < 0:
                print("Invalid Input")
            else:
                break
        while True:
            Price = float(input("Price: "))
            if Price < 0:
                print("Invalid Input")
            else:
                break
        Total_Price = Number_Of_Products * Price
        Total_Price="{:.2f}".format(Total_Price)
        print(f"{Number_Of_Products} x {Price} products = ${Total_Price}")
    elif Choice == 'Q':
        print("Farewell")
        break
    else:
        print("Invalid Choice")
print()