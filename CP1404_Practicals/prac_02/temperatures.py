"""
CP1404 - Practical Week 2 temperatures.py

Pseudocode for temperature conversion


function main():
    MENU = '""C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit""'
    display (MENU)
    get choice
    while choice != "Q":
        if choice == "C":
            fahrenheit = Celsius_To_Fahrenheit()
            display "Result: {fahrenheit:.2f} F"
        elif choice == "F":
            celsius = Fahrenheit_To_Celsius()
            display "Result: {celsius:.2f} C"
        else:
            display "Invalid option"
        display MENU
        get choice
    display "Thank you."


function Celsius_To_Fahrenheit():
    global celsius, fahrenheit
    get celsius
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


function Fahrenheit_To_Celsius():
    global fahrenheit, celsius
    get fahrenheit
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()


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
