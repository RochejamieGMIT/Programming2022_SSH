# messing with init

from distutils.command.build_scripts import first_line_re


class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def fullName(self):
        if hasattr(self, 'middlename'):
            return self.firstname +' ' + self.middlename + ' ' + self.lastname
        return self.firstname + ' ' + self.lastname

    def __str__(self) :
        return self.fullName()

    def addmiddlename(self, middlename):
        self.middlename = middlename

if __name__ == '__main__':
    person1 = Person('Jamie','Roche')

    print (person1.firstname)
    print(person1.fullName())

    person1.addmiddlename("joe")
    print(person1)