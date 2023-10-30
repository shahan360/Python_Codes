# f = open("sk.txt","a")
# a = f.write("SK toh double maja ma\n")
# print(a)
# f.close()

# f = open("sk.txt", "r+")
# print(f.read())
# a = f.write("thank you")
# print(a)

# f = open("sk.txt", "w")
# a = f.write("SK bahut achhe hain\n")
# print(a)
# f.close()

# f = open("sk.txt")
# f.seek(11)
# print(f.tell())
# print(f.readline())
# print(f.tell())
#
# print(f.readline())
# print(f.tell())
# f.close()

with open("sk.txt") as f:
    a = f.readlines()
    print(a)