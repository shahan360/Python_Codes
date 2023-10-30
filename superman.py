class A:
    clsvar1 = "I'm a clsvar in class A"
    def __init__(self):
        self.var1 = "I'm inside class A constructor"
        # self.clsvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    # clsvar1 = "I'm in class B"

    def __init__(self):
        super().__init__()
        self.var1 = "I'm inside class B constructor"
        # self.clsvar1 = "Instance var in class B"
        # super().__init__()
        # print(super().__init__())

a = A()
b = B()

# print(b.special,b.var1,b.clsvar1)
print(b.clsvar1)