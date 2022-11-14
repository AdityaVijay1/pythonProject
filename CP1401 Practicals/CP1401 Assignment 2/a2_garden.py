"""
CP1401 2022-9 Assignment 2
Market Garden Simulator
Student Name: Aditya Vijay
Date Started: 16/9/2022


Pseudocode:

LEAST_RAINFALL_POSSIBLE = 0
MAX_RAINFALL_POSSIBLE = 128
MIN_RAINFALL = 32



function main
    DAYS = 0
    PLANT_COUNT: int = 0
    TOTAL_FOOD = 0
    Plants = []
    display
        "Welcome to my garden."
        "\nPlants cost and generate food according to their name length "
        "(e.g., Sage plants cost 4)."
        "\nYou can buy new plants with the food your garden generates."
        "\nYou get up to 128 mm of rain per day. Not all "
        "plants can survive with less than 32."
        "\nEnjoy :)"
    get response
    if response == 'n':
        display "You start with these plants:\nParsley, Sage, Rosemary, Thyme, "
        Plants = ['Parsley', 'Sage', 'Rosemary', 'Thyme']
        open 'plants.txt' for writing as in_file
        for i in Plants:
            i=i+'\n'
            in_file.write(i)
        in_file.close()
    else:
        open 'plants.txt' for reading as in_file
        for i in in_file:
            Plant = i.strip('\n')
            Plants.append(Plant)
        in_file.close()

    for _ in Plants:
        PLANT_COUNT = PLANT_COUNT + 1
    display "After {DAYS} days, you have {PLANT_COUNT} plants and your total food is {TOTAL_FOOD}."
    get Choice
    while Choice != 'Q':
        if Choice == 'W':
            PLANT_COUNT, Plants, DAYS, TOTAL_FOOD = Wait(PLANT_COUNT, Plants, DAYS, TOTAL_FOOD)
        elif Choice == 'D':
            Display()
        elif Choice == 'A':
            Plants, PLANT_COUNT, TOTAL_FOOD = AddNew(PLANT_COUNT, Plants, TOTAL_FOOD)
        else:
            display "Invalid choice"
        display "After {DAYS} days, you have {PLANT_COUNT} plants and your total food is {TOTAL_FOOD}."
        get Choice

    Quit(Plants, TOTAL_FOOD, DAYS,PLANT_COUNT)


function Wait:
    # Calculating the food generated
    Rainfall = random.randint(LEAST_RAINFALL_POSSIBLE, MAX_RAINFALL_POSSIBLE)
    display "Rainfall: ", Rainfall, "mm"

    if Rainfall < MIN_RAINFALL:  # Checking if a plant will die or not
        if plants!=[]:
            Dead_Plant = random.choice(plants)
            display Dead_Plant
            if Dead_Plant in plants:
                plants.remove(Dead_Plant)
            display "Sadly, you {Dead_Plant} plant has died"
            plant_count = plant_count - 1
            open 'plants.txt' for writing as in_file
            for i in plants:
                i = i + '\n'
                in_file.write(i)
            in_file.close()
        else:
            display " You don't own any plants and no food is produced"
            main()
    Third_Of_Rainfall = int(Rainfall * (1 / 3))
    Random_Value = random.randint(Third_Of_Rainfall, Rainfall)
    # Amount of food generated
    Percent = Random_Value / MAX_RAINFALL_POSSIBLE
    for i in plants:
        Character_Count = len(i)
        Food_Generated = Percent * Character_Count
        Food_Generated = int(Food_Generated)
        total_food = Food_Generated + total_food
        display "{i} produced {Food_Generated}"

    days = days + 1
    return plant_count, plants, days, total_food

function Display
    open 'plants.txt' for reading as in_file

    for i in in_file:
        j = i.strip('\n')
        display j

    in_file.close()


function AddNew
    get Plant
    Count = 0
    if Plant not in Plants:
        for i in Plant:
            Count = Count + 1
        if Count > TOTAL_FOOD:
            display "Not enough funds to purchase this plant"
        else:
            TOTAL_FOOD = TOTAL_FOOD - Count
            Plants = Plants + [Plant]
            PLANT_COUNT = PLANT_COUNT + 1
            open 'plants.txt' for writing as in_file
            for i in Plants:
                i = i + '\n'
                in_file.write(i)
            in_file.close()
    else:
        display "You already own this plant"
    return Plants, PLANT_COUNT, TOTAL_FOOD


function Quit
    display "You finished with these plants"

    open 'plants.txt' for reading as in_file
    for i in in_file:
        j = i.strip('\n')
        display j
    display 'Now I have lots,'
    display "After {DAYS} days, you have {PLANT_COUNT} plants and your total food is {TOTAL_FOOD}."
    get Save
    if Save == 'n':
        print("Not saved.")
    else:
        open 'plants.txt' for writing as in_file
        in_file.write('')
        in_file.close()
        display "Saved."
        open 'plants.txt' for appending as in_file
        for i in Plants:
            i=i+'\n'
            in_file.write(i)
        in_file.close()


main()
"""

import random

LEAST_RAINFALL_POSSIBLE = 0
MAX_RAINFALL_POSSIBLE = 128
MIN_RAINFALL = 32


def main():
    DAYS: int = 0
    PLANT_COUNT: int = 0
    TOTAL_FOOD: int = 0
    Plants = []
    print(
        "Welcome to my garden."
        "\nPlants cost and generate food according to their name length "
        "(e.g., Sage plants cost 4)."
        "\nYou can buy new plants with the food your garden generates."
        "\nYou get up to 128 mm of rain per day. Not all "
        "plants can survive with less than 32."
        "\nEnjoy :)")
    response = input("Would you like to load your plants from plants.txt (Y/n)? ").lower()
    if response == 'n':
        print("You start with these plants:\nParsley, Sage, Rosemary, Thyme, ")
        Plants = ['Parsley', 'Sage', 'Rosemary', 'Thyme']
        in_file = open('plants.txt', 'w')
        for i in Plants:
            i = i + '\n'
            in_file.write(i)
        in_file.close()
    else:
        in_file = open('plants.txt', 'r')
        for i in in_file:
            Plant = i.strip('\n')
            Plants.append(Plant)

        in_file.close()

    PLANT_COUNT = len(Plants)
    print(f"After {DAYS} days, you have {PLANT_COUNT} plants and your total food is {TOTAL_FOOD}.")
    Choice = input("(W)ait\n(D)isplay plants\n(A)dd new plant\n(Q)uit\nChoose: ").upper()
    while Choice != 'Q':
        if Choice == 'W':
            PLANT_COUNT, Plants, DAYS, TOTAL_FOOD = Wait(PLANT_COUNT, Plants, DAYS, TOTAL_FOOD)
        elif Choice == 'D':
            Display()
        elif Choice == 'A':
            Plants, PLANT_COUNT, TOTAL_FOOD = AddNew(PLANT_COUNT, Plants, TOTAL_FOOD)
        else:
            print("Invalid choice")
        print(f"After {DAYS} days, you have {PLANT_COUNT} plants and your total food is {TOTAL_FOOD}.")
        Choice = input("(W)ait\n(D)isplay plants\n(A)dd new plant\n(Q)uit\nChoose: ").upper()

    Quit(Plants, TOTAL_FOOD, DAYS, PLANT_COUNT)


def Wait(plant_count, plants, days, total_food):
    # Calculating the food generated
    Rainfall = random.randint(LEAST_RAINFALL_POSSIBLE, MAX_RAINFALL_POSSIBLE)
    print("Rainfall: ", Rainfall, "mm")

    if Rainfall < MIN_RAINFALL:  # Checking if a plant will die or not
        if plants != []:
            Dead_Plant = random.choice(plants)
            print(Dead_Plant)
            if Dead_Plant in plants:
                plants.remove(Dead_Plant)
            print(f"Sadly, you {Dead_Plant} plant has died")
            plant_count = plant_count - 1
            in_file = open("plants.txt", 'w')
            for i in plants:
                i = i + '\n'
                in_file.write(i)
            in_file.close()
        else:
            print("You don't own any plants and no food is produced")
            main()
    Third_Of_Rainfall = int(Rainfall * (1 / 3))
    Random_Value = random.randint(Third_Of_Rainfall, Rainfall)
    # Amount of food generated
    Percent = Random_Value / MAX_RAINFALL_POSSIBLE
    for i in plants:
        Character_Count = len(i)
        Food_Generated = Percent * Character_Count
        Food_Generated = int(Food_Generated)
        total_food = Food_Generated + total_food
        print(f"{i} produced {Food_Generated}", end=", ")
    print()
    days = days + 1
    return plant_count, plants, days, total_food


def Display():
    in_file = open("plants.txt", 'r')

    for i in in_file:
        j = i.strip('\n')
        print(j, end=', ')
    print()
    in_file.close()


def AddNew(PLANT_COUNT, Plants, TOTAL_FOOD):
    Plant = input("Enter the plant to buy: ").title()
    Count = 0
    if Plant not in Plants:
        for i in Plant:
            Count = Count + 1
        if Count > TOTAL_FOOD:
            print("Not enough funds to purchase this plant")
        else:
            TOTAL_FOOD = TOTAL_FOOD - Count
            Plants = Plants + [Plant]
            PLANT_COUNT = PLANT_COUNT + 1
            in_file = open("plants.txt", 'w')
            for i in Plants:
                i = i + '\n'
                in_file.write(i)
            in_file.close()
    else:
        print("You already own this plant")
    return Plants, PLANT_COUNT, TOTAL_FOOD


def Quit(Plants, TOTAL_FOOD, DAYS, PLANT_COUNT):
    print("You finished with these plants")

    in_file = open("plants.txt", 'r')
    for i in in_file:
        j = i.strip('\n')
        print(j, end=', ')
    print('Now I have lots,')
    print(f"After {DAYS} days, you have {PLANT_COUNT} plants and your total food is {TOTAL_FOOD}.")
    Save = input("Would you like to save your plants to plants.txt (Y/n)? ").lower()
    if Save == 'n':
        print("Not saved.")
    else:
        in_file = open("plants.txt", 'w')
        in_file.write('')
        in_file.close()
        print("Saved.")
        in_file = open("plants.txt", 'a')
        for i in Plants:
            i = i + '\n'
            in_file.write(i)
        in_file.close()


main()
