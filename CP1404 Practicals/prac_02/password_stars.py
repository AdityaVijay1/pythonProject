def main():
    password = get_password()
    display_result(password)


def display_result(password):
    for i in range(len(password)):
        print('*', end='')
    print()


def get_password():
    MINIMUM_LENGTH = 5
    password = input('Enter the password: ')
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input('Enter the password: ')
    return password
main()
