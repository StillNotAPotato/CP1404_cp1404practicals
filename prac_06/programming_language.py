class ProgrammingLanguage:
    """Represent a programming language object."""
    def __init__(self, field, typing, reflection, year):
        """Initialise a programming language instance"""
        self.field = field
        self.Typing = typing
        self.Reflection = reflection
        self.Year = year

    def is_dynamic(self):
        """Return True/False if programming language is dynamically typed or not"""
        



