"""Pseudocode

function main():
    age_in_human_years = int(input("Age in human years: "))
    while age_in_human_years > 0:
        dog_years = Calculate_Dog_Years(age_in_human_years)
        print("In dog years the age is:", dog_years)
        print()
        age_in_human_years = int(input("Age in human years: "))


function Calculate_Dog_Years(human_years):
    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 21 + 4 * (human_years - 2)
    return dog_years

main()
"""


def main():
    age_in_human_years = int(input("Age in human years: "))
    while age_in_human_years > 0:
        dog_years = Calculate_Dog_Years(age_in_human_years)
        print("In dog years the age is:", dog_years)
        print()
        age_in_human_years = int(input("Age in human years: "))


def Calculate_Dog_Years(human_years):
    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 21 + 4 * (human_years - 2)
    return dog_years


main()
