"""CP1404 Practicals
Guitar
Estimate Time: 30 minutes
Actual Time: 35 minutes"""


CURRENT_YEAR=2022
MINIMUM_AGE=50
class Guitar:
    def __init__(self,name='',year=0,cost=0.0):
        self.name=name
        self.year=year
        self.cost=cost
    def __str__(self):
        return f"{self.name} ({self.year}) : {self.cost:,.2f}"
    def get_age(self):
        return CURRENT_YEAR-self.year
    def is_vintage(self):
        if self.get_age()>=MINIMUM_AGE:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.year < other.year
