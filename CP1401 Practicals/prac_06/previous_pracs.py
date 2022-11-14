""" 4. Add Functions to Previous Pracs

function main1():
    worker_level = get_Number()
    worker_level_check= is_Worker_Level_Valid(worker_level)
    salary=calculate_salary(worker_level_check)
    display "With worker level {worker_level}, your salary is ${salary:,.2f}"


function get_number():
    Number=int(input("Enter number: "))
    return Number


function is_worker_level_valid(worker_level):
    while worker_level < 1 or worker_level > 10:
        print("Invalid worker level")
        worker_level = int(input("Worker level: "))
    return worker_level


function calculate_Salary(worker_level):
    salary = worker_level * 5000
main1()




function main2():
    Number_of_rows = get_Number()
    Number_of_columns = get_Number()
    print("Rows:", Number_of_rows)
    print("Columns:", Number_of_columns)
    Display_Grid(Number_of_rows,Number_of_columns)
function Display_Grid(Rows,Columns):
    for i in range(Rows):
        for j in range(Columns):
            print(j, end=' ')
main2()


"""


def main1():
    worker_level = get_number()
    worker_level_check = is_worker_level_valid(worker_level)
    salary = calculate_salary(worker_level_check)
    print(f"With worker level {worker_level_check}, your salary is ${salary:,.2f}")


def get_number():
    number = int(input("Enter number: "))
    return number


def is_worker_level_valid(worker_level):
    while worker_level < 1 or worker_level > 10:
        print("Invalid worker level")
        worker_level = int(input("Worker level: "))
    return worker_level


def calculate_salary(worker_level):
    salary = worker_level * 5000
    return salary


main1()
print()

print("Next Program")


def main2():
    number_of_rows = get_number()
    number_of_columns = get_number()
    print("Rows:", number_of_rows)
    print("Columns:", number_of_columns)
    display_grid(number_of_rows, number_of_columns)


def display_grid(rows, columns):
    for i in range(rows):
        for j in range(columns):
            print(j, end=' ')
        print()


main2()
