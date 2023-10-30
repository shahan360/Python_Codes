# l = 10


def function1(n):
    # l = 5
    m = 8
    global l
    print(l, m)
    print(n, "I have printed")


# function1("This is me")
# print(m)

x=89
def sk():
    x = 20
    def bh():
        global x
        x = 88
        print(x)

    print("before calling bh()", x)
    bh()
    print("after calling bh()", x)


sk()
# print(x)
