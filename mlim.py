class ElectronicGadgets():
    components = 4
    _protec = 9
    __priv = 99
    def __init__(self,dname):
        self.name = dname
    def eFunct(self):
        return f"This {self.name} runs electronic codes."
    # pass

class PocketDevices(ElectronicGadgets):
    # components = 6
    def __init__(self,dname,dtype,dcode):
        self.name = dname
        self.type = dtype
        self.code = dcode

    def eUse(self):
        return f"This {self.name} is a portable device. Its use is {self.type}."
    # pass

class Mobile(PocketDevices):
    # components = 8
    def eUse(self):
        return f"This {self.name} is a portable device. Its use is {self.type}.Its code is written in {self.code}"
    # pass

electri = ElectronicGadgets("Computer")

mp3player = PocketDevices("ipod","music player","c++")

nokia3110 = Mobile("Nokia","cell phone","Java")

print(electri.eFunct())
print(mp3player.eUse())
print(nokia3110.eUse())
print(nokia3110.components)
print(nokia3110._protec)
print(nokia3110._ElectronicGadgets__priv)