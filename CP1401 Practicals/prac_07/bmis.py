"""Pseudocode
function main():
    HEIGHT=1.75
    for i in range(50,101,2):
        bmi=calculate_bmi(HEIGHT,i)
        reply=determine_weight_category(bmi)

        print(f"Height {HEIGHT}m, Weight {i}kg = BMI {bmi:.1f} considered {reply}")
    print()
    for i in range(150,191,10):
        i=i/100
        for j in range(50,101,10):
            bmi=calculate_bmi(i,j)
            reply=determine_weight_category(bmi)
            print(f"Height {i}m, Weight {j}kg = BMI {bmi:.1f} considered {reply}")
    print()


function calculate_bmi(height, weight):
    return weight / (height ** 2)


function determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


main()

"""


def main():
    HEIGHT = 1.75
    for i in range(50, 101, 2):
        bmi = calculate_bmi(HEIGHT, i)
        reply = determine_weight_category(bmi)

        print(f"Height {HEIGHT}m, Weight {i}kg = BMI {bmi:.1f} considered {reply}")
    print()
    for i in range(150, 191, 10):
        i = i / 100
        for j in range(50, 101, 10):
            bmi = calculate_bmi(i, j)
            reply = determine_weight_category(bmi)
            print(f"Height {i}m, Weight {j}kg = BMI {bmi:.1f} considered {reply}")
    print()


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
