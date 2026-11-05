# Worksheet 1.5: Person class

from datetime import date
class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """ Creates A Person with name and birthdate provided """
        if (type(name) != str) or (type(birth) != date):
            raise TypeError
        if name == "":
            raise ValueError
        self.name = name
        self.birth = birth
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def initials(self):
        """Returns Capitalised values in name"""
        i = 1
        initials = self.name[0].upper()
        for i in range(1, len(self.name)):
            if self.name[i-1] == " ":
                initials = initials + self.name[i].upper()
        return initials
    def is_birthday(self):
        """Returns true if current date is birthday, else false"""
        if self.birth.month == date.today().month and self.birth.day == date.today().day:
            return True
        else:
            return False
"""Freddie = Person("freddie ash money", date.today())
print(Freddie.is_birthday())
print(Freddie.initials())"""
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
