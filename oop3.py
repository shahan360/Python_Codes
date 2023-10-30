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

    @classmethod
    def from_dog(cls,string):
        params = string.split("-")
        print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is a good "+string)

class Mammals(Animals):
    var = 8

    def __init__(self,aname,astrength,alimbs,askills):
        self.name = aname
        self.strength = astrength
        self.limbs = alimbs
        self.skills = askills

    def printMdetails(self):
        return f"The mammal name is {self.name}. The strength level is {self.strength}.The limbs number is {self.limbs}. The skills are {self.skills}"

class Habitable():
    var = 9

    def __init__(self,aname):
        self.name = aname
    def isHabitable(self):
        print(f"The Animal {self.name} is habitable.")

class DomAnimal(Mammals,Habitable):
    # var = 10
    pass


# tiger = Animals("Bonga","SuperDuper",6)

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

# parrot = Animals("Moti","Low",2)
#
# print(parrot.printdetails())
# print(parrot.name)
# print(parrot.no_of_brain)
#
# print(parrot.change_brain(3))
# print(parrot.no_of_brain)
# print(tiger.no_of_brain)

# dog = Animals.from_dog("Molu-Very High-4")
# print(dog.no_of_brain)

# Animals.printgood("Dog")

# horse = Mammals("Oliver","Supreme","4",["Running","Jumping"])
#
# print(horse.printMdetails())
# print(horse.skills)

dogesh = DomAnimal("Kongo","Okay",5,["Barking","Talking"])

dogesh.isHabitable()
print(dogesh.var)