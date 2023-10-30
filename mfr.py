# -----------MAP----------
# num = ["2","5","7"]

# for i in range(len(num)):
#     num[i]=int(num[i])

# num = list(map(int,num))
#
# num[2]=num[2]+1
# print(num[2])
#
# def sq(a):
#     return a*a
#
# num2 = [2,3,5,6,76,3,3,2]
# sq2 = list(map(sq,num2))
# print(sq2)
# sq3 = list(map(lambda x:x*x,num2))
# print(sq3)
#
# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [square,cube]
# for i in range(5):
#     val = list(map(lambda x:x(i),func))
#     print(val)

#-------------FILTER---------------
# list_1 = [1,2,3,4,5,6,7,8,9]
#
# def greater_t_5(n):
#     return n>5
#
# grt_t_5 = list(filter(greater_t_5,list_1))
# print(grt_t_5)

#-------------REDUCE----------------
from functools import reduce
list1 = [1,2,3,4,2]
num = reduce(lambda x,y:x+y,list1)
print(num)
