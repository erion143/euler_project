def product(l):
    res = 1
    for i in l:
        res *= i
    return res

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
