# book list program
# importing library
import csv


# defining a function to write data in csv
def write_csv(data):
    with open("booklist.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data)


# defining a function to read data from csv
def read_csv():
    with open("booklist.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        book_list = []
        for row in reader:
            book_list.append(row)
        return book_list


# defining a function to sort data based on author and title
def sort_data(book_list):
    book_list.sort(key=lambda x: (x[1], x[0]))


# defining a function to print sorted data
def print_data(book_list):
    for i in range(len(book_list)):
        print("{}-{}({},pages) {:^20} {:^20}".format(i + 1, book_list[i][0], book_list[i][1], book_list[i][2],
                                                     book_list[i][3]))


# defining a function to add new record
def add_record(book_list):
    title = input("enter the title of book : ")
    author = input("enter the author of book : ")
    pages = input("enter the total pages of book : ")
    req = input("is it required? (y/n) : ")
    data = [title, author, pages, req]
    book_list.append(data)
    write_csv(data)


# defining a function to mark book as read
def mark_as_read(book_list):
    book_number = int(input("enter the book number : "))
    book_list[book_number - 1][3] = "yes"
    write_csv(book_list[book_number - 1])


# defining a function to delete book
def delete_book(book_list):
    book_number = int(input("enter the book number : "))
    book_list.pop(book_number - 1)


# defining a function to show the menu
def show_menu():
    print("1. Print book list")
    print("2. Add record")
    print("3. Mark as read")
    print("4. Delete book")
    print("5. Exit")


# initializing empty list
book_list = []

# main program
while True:
    show_menu()
    choice = int(input("enter the choice : "))
    if choice == 1:
        book_list = read_csv()
        sort_data(book_list)
        print_data(book_list)
    elif choice == 2:
        add_record(book_list)
    elif choice == 3:
        mark_as_read(book_list)
    elif choice == 4:
        delete_book(book_list)
    elif choice == 5:
        break
    else:
        print("invalid choice")
