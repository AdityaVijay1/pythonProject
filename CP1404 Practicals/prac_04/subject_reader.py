"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    FILENAME = 'subject_data.txt'
    data = get_data(FILENAME)
    final_data=process_data(data)
    print(final_data)

    for value in final_data:
        print(f"{value[0]} is taught by {value[1]} and has {value[2]} students")


def get_data(FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    line=input_file.readlines()
    input_file.close()
    return line


def process_data(data):
    lines = []
    for line in data:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        lines.append(parts)
        print("----------")
    return lines


main()
