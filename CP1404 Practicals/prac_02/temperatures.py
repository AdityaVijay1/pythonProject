"""
CP1404 - Practical Week 1 temperature.py

Pseudocode for temperature conversion

MENU = ""C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit""
display MENU
get choice
while choice != "Q":
    if choice == "C":
        get celsius
        fahrenheit = celsius * 9.0 / 5 + 32
        display "Result: {fahrenheit:.2f} F"
    elif choice == "F":
        get fahrenheit
        celsius = 5 / 9 * (fahrenheit - 32)
        display "Result: {celsius:.2f} C"
    else:
        display "Invalid option"
    display MENU
    get choice
display "Thank you."

"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = Celsius_To_Fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = Fahrenheit_To_Celsius()
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def Celsius_To_Fahrenheit():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def Fahrenheit_To_Celsius():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
