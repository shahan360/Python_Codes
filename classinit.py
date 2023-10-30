class Student:
    def __init__(self, aname, aroll, aage, acls):
        self.name = aname
        self.roll = aroll
        self.age = aage
        self.cls = acls
    def details(self):
        print(f'{self.name} is a student of {self.cls} with roll no. {self.roll} and age {self.age}.')

shakti = Student('Shakti', 25, 15, 'Sixth')
shakti.details()