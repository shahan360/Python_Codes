class Animals:
    no_of_brain = 1

    def __init__(self,aname,astrength,alimbs):
        self.name = aname
        self.strength = astrength
        self.limbs = alimbs

    def printdetails(self):
        return f"The Animal name is {self.name}. Strength is {self.strength}. Number of limbs are {self.limbs}."

    @classmethod
    def change_brain(cls,newnumber):
        cls.no_of_brain=newnumber

tiger = Animals("Bonga","SuperDuper",6)

# tiger = Animals()
# whale = Animals()
#
# tiger.name = "Shera"
# tiger.strength = "Supreme"
# tiger.limbs = 4
# tiger.sense6 = True
#
# whale.name = "Donna"
# whale.strength = "High"
# whale.gills = True
# whale.limbs = 2
# whale.no_of_brain =2
# print(tiger.no_of_brain)
# print(whale.no_of_brain)
# print(tiger.__dict__)
# print(whale.__dict__)
# print(Animals.__dict__)

# print(whale.printdetails())
# print(tiger.printdetails())

parrot = Animals("Moti","Low",2)

print(parrot.printdetails())
print(parrot.name)
print(parrot.no_of_brain)

print(parrot.change_brain(3))
print(parrot.no_of_brain)
print(tiger.no_of_brain)


