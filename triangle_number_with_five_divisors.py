from compare import compare
from primeFactor import factorisation

def triangle_number(n):
    return sum(range(1, n+1))

def divisors(n):
    ret = []
    for i in range(1, n+1):
        if n % i == 0:
            ret.append(i)
    print(ret)
    return len(ret)

def direct(n):
    cur = triangle = 0
    mmax = (0, 0)
    while True:
        cur += 1
        triangle += cur
        div = divisors(triangle)
        if len(div) >= mmax[1]:
            mmax = (triangle, len(div))
            if mmax[1] >= n:
                return triangle, cur
        if not cur % 1000:
            print(cur, triangle, mmax)

def to_full(l):
    foo = {}
    for i in l:
        if not i in foo:
            foo[i] = 1
        else:
            foo[i] += 1
    ret = []
    for i in foo:
        ret += [i ** j for j in range(1, foo[i]+1)]
    print(ret)
    return len(ret) - 1

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

def comb(n, k):
    return fact(n) / fact(k) / fact (n - k)

def full(n):
    divs = factorisation(n)
    sorted(divs)

def not_so_direct(n):
    cut = triangle = 0
    f = factorisation(n)
    

if __name__ == '__main__':
    compare(5*5*5*5*7, divisors)
