"""
Coffee Orders- All Together now
"""
import random
MENU = "(O)rder - (D)rink - (R)andom choice - (Q)uit"
COFFEES = ["Flat White", "Espresso", "Long Black", "Babyccino"]


def main():
    coffee = ""
    print("Welcome to the IT@JCU Coffee Shop ")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "O":
            coffee = get_order()
            instructions(coffee)
        elif choice == "D":
            if coffee == "":
                print("Oh... where's my coffee?")
            else:
                print(f"Mmmm, nice {coffee}")
        elif choice=="R":
            coffee=random.choice(COFFEES)
            instructions(coffee)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


def get_order():
    print("Please choose from: ")
    for coffee in COFFEES:
        print(coffee, end=' - ')
    coffee_choice = input("? ").title()
    while coffee_choice not in COFFEES:
        print("Invalid order")
        coffee_choice = input("? ").title()
    return coffee_choice

def instructions(coffee):
    print(f"Here's how to make a/n {coffee}")
    if coffee=="Espresso":
        grind_beans()
        pour_espresso()
    elif coffee=="Long Black":
        grind_beans()
        pour_espresso()
        print("-  Add hot water to cup")
    elif coffee=="Flat White":
        grind_beans()
        pour_espresso()
        steam_milk()
        add_milk()
    elif coffee=="Babyccino":
        steam_milk()
        add_milk()
    else:
        print("Something went wrong! Unknown coffee.")

def grind_beans():
    print("- Insert portafilter into the grinder")
    print("- Press grind button to grind beans into portafilter")

def pour_espresso():
    print("- Distribute grounds")
    print("- Tamp grounds")
    print("- Insert full portafilter into group head")
    print("- Press shot button to pour espresso into cup")

def steam_milk():
    print("- Fill jug with milk")
    print("- Steam milk until nice microfoam formed and milk up to temperature")

def add_milk():
    print("- Swirl milk gently in jug")
    print("- Pour milk into cup... carefully, artistically :)")


main()