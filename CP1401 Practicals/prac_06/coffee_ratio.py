"""1. Coffee Brew Ratio
function main():
    Dose, Yield = get_Dose_and_Yield()
    RatioDose, RatioYield = determine_ratio(Dose, Yield)
    Coffee_Style = determine_style(RatioYield)
    display "{RatioDose}:{RatioYield} is considered {Coffee_Style}"

function get_Dose_and_Yield():
    get Number1
    if Number1>100 or Number1<0:
        display "Invalid Input"
        get Number1
    get Number2
    if Number2>100 or Number2<0:
        display "Invalid Input"
        get Number2
    return Number1, Number2


function determine_ratio(Dose, Yield):
    Ratio_Value = Yield / Dose
    DoseValue = int(Dose / Dose)
    return DoseValue, Ratio_Value


function determine_style(number):
    if number < 2:
        Style = 'ristretto'
    elif number < 3:
        Style = 'normale'
    else:
        Style = 'lungo'
    return Style


main()

"""


def main():
    Dose, Yield = get_Dose_and_Yield()
    RatioDose, RatioYield = determine_ratio(Dose, Yield)
    Coffee_Style = determine_style(RatioYield)
    print(f"{RatioDose}:{RatioYield} is considered {Coffee_Style}")


# def get_style(2.7):
#     if number <= 2:
#         Style = 'ristretto'
#     elif number<=3:
#         Style='normale'
#     else:
#         Style='lungo'
#     return Style

def get_Dose_and_Yield():
    Number1 = float(input("Dose: "))
    if Number1>100 or Number1<0:
        print("Invalid Input")
        Number1 = float(input("Dose: "))
    Number2 = float(input("Yield: "))
    if Number2>100 or Number2<0:
        print("Invalid Input")
        Number2 = float(input("Yield: "))
    return Number1, Number2


def determine_ratio(Dose, Yield):
    Ratio_Value = Yield / Dose
    Ratio_Value='{:.1f}'.format(Ratio_Value)
    Ratio_Value=float(Ratio_Value)
    DoseValue = int(Dose / Dose)
    return DoseValue, Ratio_Value


def determine_style(number):
    if number < 2:
        Style = 'ristretto'
    elif number < 3:
        Style = 'normale'
    else:
        Style = 'lungo'
    return Style
main()
