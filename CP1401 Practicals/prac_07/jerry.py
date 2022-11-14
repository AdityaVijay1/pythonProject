"""Psuedocode

function main():
    speed_in_mph = get_valid_number("Speed in mph: ")
    speed_limit_in_kph = get_valid_number("Speed limit in kph: ")
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    fine = determine_fine(speed_in_kph, speed_limit_in_kph)
    display"Your fine is",fine


function get_valid_number(prompt):
    number = float(input(prompt))
    while number < 0 or number > 300:
        number = float(input(prompt))
    return number


function convert_miles_to_km(speed_in_mph):
    KILOMETRE = 1.60934
    speed_in_kph = KILOMETRE * speed_in_mph
    return speed_in_kph


function determine_fine(speed_in_kph, speed_limit_in_kph):
    speed_difference = speed_in_kph - speed_limit_in_kph
    if speed_difference < 13:
        return 177
    elif speed_difference < 20:
        return 266
    elif speed_difference < 30:
        return 444
    elif speed_difference < 40:
        return 622
    else:
        return 1245


main()
"""


def main():
    speed_in_mph = get_valid_number("Speed in mph: ")
    speed_limit_in_kph = get_valid_number("Speed limit in kph: ")
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    fine = determine_fine(speed_in_kph, speed_limit_in_kph)
    print(f"Your fine is ${fine}")


def get_valid_number(prompt):
    number = float(input(prompt))
    while number < 0 or number > 300:
        number = float(input(prompt))
    return number


def convert_miles_to_km(speed_in_mph):
    KILOMETRE = 1.60934
    speed_in_kph = KILOMETRE * speed_in_mph
    return speed_in_kph


def determine_fine(speed_in_kph, speed_limit_in_kph):
    "Calculates the fine"
    speed_difference = speed_in_kph - speed_limit_in_kph
    if speed_difference < 13:
        return 177
    elif speed_difference < 20:
        return 266
    elif speed_difference < 30:
        return 444
    elif speed_difference < 40:
        return 622
    else:
        return 1245


main()
