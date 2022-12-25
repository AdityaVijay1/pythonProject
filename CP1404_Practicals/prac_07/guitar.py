"""CP1404 Practicals
guitar program
Estimate Time: 30 minutes
Actual Time: 35 minutes"""

CURRENT_YEAR = 2022
MINIMUM_AGE = 50


class Guitar:
    def __init__(self, name='', year=0, cost=0.0):
        """Initialise a Guitar instance.

                name: Name of the guitar
                year: Year of the guitar
                cost: Cost of the guitar
                """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : {self.cost:,.2f}"

    def get_age(self):
        """ Get the age of the guitar in the current year """
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """ Find out weather the guitar is a vintage one or not"""
        if self.get_age() >= MINIMUM_AGE:
            return True
        else:
            return False

    def __lt__(self, other):
        """ Method to compare the two guitar based on the year"""
        return self.year < other.year
