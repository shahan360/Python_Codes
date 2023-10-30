class A:
    def met(self):
        print("This method is from class A")

class B(A):
    def met(self):
        print("This method is from class B")

class C(A):
    def met(self):
        print("This method is from class C")

class D(B,C):
    pass
    # def met(self):
    #     print("This method is from class D")

a = A()
b = B()
c = C()
d = D()

d.met()