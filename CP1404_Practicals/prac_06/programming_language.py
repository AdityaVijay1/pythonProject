"""CP1404 Practicals
Programming Language
Estimate Time: 20 minutes
Actual Time: 15 minutes"""


class ProgrammingLanguage:
    def __init__(self, name='', typing='', reflection= bool, year=0):
        """Initialise a Guitar instance.

                        name: Name of the programming language
                        typing: Type of programming language
                        reflection: Reflection of the programming language
                        year: Year of the programming language released
                        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name},{self.typing} Typing, Reflection= {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Method to find out which programming language is dynamic"""
        if self.typing == 'Dynamic':
            return True
        else:
            return False


