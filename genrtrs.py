def ginti(n):
    for i in range(n):
        yield i

g = ginti(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

h = "Shasha"

ier = iter(h)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
for c in h:
    print(c)