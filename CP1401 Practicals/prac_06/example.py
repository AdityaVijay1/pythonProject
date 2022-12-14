def main():
    height = get_valid_number("Height (m): ", 0, 3)
    weight = get_valid_number("Weight (kg): ", 0, 300)
    age = get_valid_number("Age (y): ", 20, 120)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print(f"This BMI is {bmi}, which is considered {category}")


def calculate_bmi(height, weight):
    return weight / (height ** 2)


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def calculate_bmi(height, weight):
    return weight / (height ** 2)


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


main()
