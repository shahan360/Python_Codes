# def function1():
#     print("Subscribe now")
#
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
# a = funcret(1)
# print(a)

# def executor(func):
#     return func([1,2])
# print(executor(sum))

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

def dec2(func2):
    def mk():
        print("SK is SK")
        func2()
        print("SK is now KS")
    return mk

@dec1
def who_is_sk():
    print("SK is Genius")

@dec2
def more_sk():
    print("SK can make you dance")
    print("SK is very talented")

#who_is_sk = dec1(who_is_sk)

# who_is_sk()

more_sk()