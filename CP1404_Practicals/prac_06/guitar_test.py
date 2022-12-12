"""CP1404 Practicals
Guitar_Test
Estimate Time: 15 minutes
Actual Time: 10 minutes"""

from CP1404_Practicals.prac_06.guitar import Guitar


def main():
    guitar1=Guitar("Gibson L-5 CES",1922,16035.40)
    guitar2=Guitar("Line 6 JTV-59",2010,1512.90)
    guitar3=Guitar("Fender Stratocaster", 2014, 765.40)
    print(guitar1)
    print(guitar2)
    print(guitar3)
    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 12. Got {guitar2.get_age()}")
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")
main()