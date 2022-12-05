"""
CP1404/CP5632 Practical

Hex Colours
Estimate: 15 minutes
Actual:   10 minutes
"""


COLOR_TO_CODE = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "Aqua": "#00ffff",
    "Army Green": "#4b5320",
    "Banana Mania": "#fae7b5",
    "Barn Red": "#7c0a02",
    "Beaver": "#9f8170",
    "Beige": "#f5f5dc",
    "Bitter Lime": "#bfff00",
}
print(COLOR_TO_CODE)
for i in COLOR_TO_CODE:
    print(f"{i} is {COLOR_TO_CODE[i]}")
print()

color_name = input("Enter color's name: ").title()
while color_name != "":
    if color_name in COLOR_TO_CODE:
        print(color_name, "is",COLOR_TO_CODE[color_name])
    else:
        print("Invalid colour name")
    color_name = input("Enter color's name: ").title()
print("Farewell")

