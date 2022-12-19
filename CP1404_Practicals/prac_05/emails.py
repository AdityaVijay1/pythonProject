"""
Emails
Estimate: 20 minutes
Actual:   30 minutes
"""


def main():
    information = {}
    email_id = input("Email: ")
    while email_id != "":
        details = get_name(email_id)
        if len(details) > 1:
            full_name = ''
            for i in range(0, len(details)):
                full_name = full_name + details[i].title() + " "
            name_inquiry(full_name,information,email_id)
        else:

            name_inquiry(details[0],information,email_id)

        email_id = input("Email: ")
    display_results(information)

def name_inquiry(name,information,email_id):
    name_confirmation = input(f"Is your name {name.title()}? (Y/n) ").lower()
    if name_confirmation == 'n' or name_confirmation == 'no':
        name = input("Name: ")
        information[name] = email_id
    else:
        information[name_confirmation] = email_id

def get_name(email_id):
    separator = email_id.index("@")
    return "".join(i for i in email_id[:separator]).split(".")


def display_results(information):
    for i in information:
        print(f"{i} ({information[i]})")


main()
