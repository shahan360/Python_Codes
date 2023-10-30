class Animals:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

    def explain(self):
        return f"This animal is {self.fname} {self.lname}"


animal_supporter = Animals("Sher","Singh")

# print(animal_supporter.explain())
print(animal_supporter.email)
animal_supporter.fname = "Tiger"
print(animal_supporter.email)

animal_supporter.email = "Peckock.More@codewithharry.com"
print(animal_supporter.fname)

del animal_supporter.email
print(animal_supporter.email)
animal_supporter.email = "SK.GK@codewithharry.com"
print(animal_supporter.email)

skillf = Animals("Skill","F")
# o="this is a string"
# print(dir(skillf))
# print(id(o))
# print(id("that_that"))

# import inspect
# print(inspect.getmembers(skillf))
