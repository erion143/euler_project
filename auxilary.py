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

def flat(l):
    return [j for i in l for j in i]

print(flat([[1,2,3], [2,3,4], [1]]))
