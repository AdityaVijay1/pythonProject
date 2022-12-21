import csv
from guitar import Guitar


def main():
    """Read file of programming language details, save as objects, display."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        write_to_file(name, year, cost)
        name = input("Name: ")
    print("These are my guitars:")
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    # File format is like: Name,Year, Cost
    # 'Consume' the first line (header) - we don't need its contents
    #     in_file.readline()
    #     #ts  All other lines are language data
    for line in in_file:
        parts = line.strip().split(',')
        # print(parts)  # debugging

        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    # Loop through and display all languages (using their str method)



def write_to_file(name, year, cost):
    with open('guitars.csv', 'a') as out_file:
        print(f"{name},{year},{cost}", file=out_file)


main()
