def question_1():
    for i in range(40):
        print('-', end='')
    print()


def question_2():
    some_number = int(input("Number: "))
    if is_even(some_number):
        print(f"{some_number} is even")
    else:
        print(f"{some_number} is odd")


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def question_3():
    name = get_string("Enter your name: ")
    birthplace = get_string("Enter your birthplace: ")
    print(f"Hi {name} from {birthplace}")


def get_string(prompt):
    response = input(prompt)
    return response


def question_4():
    min_number = int(input('Minimum number: '))
    max_number = get_valid_number(min_number, 'Maximum number: ')
    numbers = []
    for i in range(min_number, max_number + 1):
        numbers.append(i)
    print(numbers)


def get_valid_number(number, prompt):
    max_number = int(input(prompt))
    while max_number <= number:
        print(f"Your maximum number must be greater than {number}")
        max_number = int(input(prompt))
    return max_number


def question_5():
    subject_code = get_string('Enter subject code: ').upper()
    subjects = []
    while subject_code != '':
        if check_length(subject_code) and check_letter(subject_code) and check_digit(subject_code):
            subjects.append(subject_code)
            subject_code = get_string('Enter subject code: ').upper()
        else:
            print("Invalid choice")
            subject_code = get_string('Enter subject code: ').upper()
    count = len(subjects)
    print(f"You do these {count} subjects")
    for i in subjects:
        print(i)
    if 'CP1401' in subjects:
        print("You are cool")


def check_length(subject_code):
    if len(subject_code) == 6:
        return True
    else:
        return False


def check_letter(subject_code):
    if subject_code[0:2].isalpha():
        return True
    else:
        return False


def check_digit(subject_code):
    if subject_code[2:6].isdigit():
        return True
    else:
        return False


question_1()
question_2()
question_3()
question_4()
question_5()
