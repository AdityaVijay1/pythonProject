def main():
    number_of_people=int(input("Enter the number of people: "))
    file_name=open("bmis.txt",'w')
    file_name.write('')
    file_name.close()
    for i in range(0,number_of_people):
        file_name=open("bmis.txt",'a')
        height = get_valid_number("Height: ", 0, 3)
        weight = get_valid_number("Weight: ", 0, 300)
        bmi = calculate_bmi(height, weight)
        file_name.write(str(bmi)+'\n')
        file_name.close()
    file_name=open("bmis.txt",'r')
    for i in file_name:
        bmi=float(i)
        category = determine_weight_category(bmi)
        print(f"BMI {bmi:.1f}, considered {category}")
    file_name.close()
def calculate_bmi(height, weight):
    return weight / (height ** 2)


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number




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