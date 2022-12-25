"""
Replace the contents of this module docstring with your own details
Name: Aditya Vijay
Date started: 20th December, 2022
GitHub URL: https://github.com/JCUS-CP1404/cp1404-reading-tracker---assignment-1-AdityaVijay1
"""
import csv

MENU = "Menu:\nL - List all books\nA - Add new book\nM - Mark a book as completed\nQ - Quit"


def main():
    """..."""
    print("Reading Tracker 1.0 - by Aditya Vijay")
    books = read_file()
    print(f"{len(books)} books loaded")
    choice = get_choice()
    while choice != 'Q':
        if choice == 'L':
            longest_book_name,longest_author_name=get_alignment(books)

            for index, row in enumerate(books, 1):
                required = check_required(row[3])
                print(f"{required}{index}.{row[0]:<{longest_book_name}} by {row[1]:<{longest_author_name}} {row[2]} pages")
        elif choice == 'A':
            pass
        elif choice == 'M':
            pass
        else:
            print("Invalid menu choice")
        choice = get_choice()

def read_file():
    with open("books.csv", "r") as in_file:
        reader = csv.reader(in_file)

        books = []
        for row in reader:
            books.append(row)
        return books


def get_choice():
    print(MENU, end='\n')
    choice = input('>>> ').upper()
    return choice


def check_required(value):
    if value == 'r':
        return '*'
    else:
        return ' '
def get_alignment(books):
    count_book=0
    count_author=0
    for row in books:
        if len(row[0])>count_book:
            count_book=len(row[0])
        if len(row[1])>count_author:
            count_author=len(row[1])
    return count_book,count_author
if __name__ == '__main__':
    main()
