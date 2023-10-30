# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

# ls = [i for i in range(100) if i%3==0]
#
# print(ls)
#
# dict1 = {i:f"Case {i}" for i in range(5)}
# print(dict1)
#
# dict2 = {v:k for k,v in dict1.items()}
# print(dict2)
# print(dict1,"\n",dict2)

# dresses = {dress for dress in ["dress1", "dress2","dress1",
#                                "dress2","dress1", "dress2"]}
# print(dresses)
# print(type(dresses))

evens = (i for i in range(100) if i%2==0)
print(evens.__next__())
print(type(evens))