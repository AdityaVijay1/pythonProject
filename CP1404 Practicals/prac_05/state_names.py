"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}
print(CODE_TO_NAME)
for i in CODE_TO_NAME:
    print(f"{i} is {CODE_TO_NAME[i]}")
print()

state_code = input("Enter short state: ").upper()
state_codes=[]
while state_code != '':
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
        state_codes.append(state_code)
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
for i in state_codes:
    print(f"{i} is {CODE_TO_NAME[i]}")
