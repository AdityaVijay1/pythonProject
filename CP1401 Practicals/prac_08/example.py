"""Pseudocode
CP1401-Practical 8- Example

places = []
longest_place = ''
get place.title()
while place != "":
    if len(place) > len(longest_place):
        longest_place = place
    places.append(place)
    get place.title()
if places == []:
    display"I went nowhere :("
else:
    display "On my holiday, I went to: "
    for place in places:
        display place
        if len(place) > len(longest_place):
            longest_place = place

    display longest_place
"""

places = []
longest_place = ''
place = input("Place: ").title()
while place != "":
    places.append(place)
    place = input("Place: ").title()
if places == []:
    print("I went nowhere :(")
else:
    print("On my holiday, I went to: ")
    for place in places:
        print(place)
        if len(place) > len(longest_place):
            longest_place = place

    print("The place with the longest name was", longest_place)
