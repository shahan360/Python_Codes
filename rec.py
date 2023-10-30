n = int(input("Enter a number: "))

def fact_rec(n):
    if n==1:
        return 1
    else:
        return n*fact_rec(n-1)

print("The factorial of ",n," is ",fact_rec(n))

def fibo_sum(n):
    if n ==1:
        return 0
    elif n ==2:
        return 1
    else:
        return fibo_sum(n-1)+fibo_sum(n-2)

print("The fibonacci sum of ",n," is ",fibo_sum(n))