from compare import compare
from time import time
from math import sqrt
from random import randint
from primes import is_it_prime

'''
# 003
What is the largest prime factor of the number 600851475143 ?
'''

def roundup(n):
    return int(n) + (n % 1 > 0)

def direct(n):
    for i in range(int(n // 2 + (n % 2 == 0)), 0, -2):
        if n % i == 0:
            if is_it_prime(i):
                return i
            else:
                continue

def factorisation(n, factors=[]):
    for i in range(2, int(n//2)):
        if n % i == 0:
            factors.append(i)
            return factorisation(n // i, factors=factors)
    else:
        return factors + [n]

def fermat(n, main=True):
    #print('run', n, ':', end=' ')
    if n % 2 == 0: # с четными числами у меня не работает, поэтому
                   # сперва раскладываем до нечетного
        return sorted([2, ] + fermat(n / 2, main=False))
    y = sqrt(n)       # проверяем, является ли 
    if y == int(y):   # само число квадратом
        if main:
            return sorted(fermat(y, main=False) + fermat(y, main=False))
        else:
            return fermat(y, main=False) + fermat(y, main=False)
    # -------- Сам алгоритм -----------
    # n = X^2 - Y^2 = (X + Y) * (X - Y)
    # Y^2 = X^2 - n
    # Раввенство имеет смысл, если X >= roundup(sqrt(n))
    # Пусть X = S + K, где S = roundup(sqrt(n)), а K = 0, 1, 2, ...
    # Если Y - целое число, то (S + K - Y) И (S + K + Y) - делители числа n
    s = roundup(sqrt(n))
    k = 0
    while True:
        yy = (s + k) ** 2 - n
        y = sqrt(yy)
        if y == int(y):
            if s + k - y == 1: # Если число простое
                return [n, ]   # Единица не включается в список множителей
            else:              # Если число составное, произв. рекурсивный вызов 
                if main:       # для обоих множителей
                    return sorted(fermat(s + k + y, main=False)
                                  + fermat(s + k - y, main=False))
                else:
                    return (fermat(s + k + y, main=False)    # Больший множитель
                            + fermat(s + k - y, main=False)) # Меньший множитель
        else:
            k += 1
    # ---------------------------------
        if k >= n:
            print('something has gone wrong')
            break

def euclid(a, b):
    #print('run with', a, b)
    # Алгоритм Евклида для нахождения НОД
    if a < b:
        a, b = b, a
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b

def pollard_floyd_one(n, x0):
    #print('one run with', n, x0)
    def f(x, a=1):
        return x*x + a

    x = y = x0
    i = 0
    while True:
        #print('pollard cur', x, y)
        x = f(x) % n
        y = f(f(y) % n) % n
        if x == y:
            return 1
        #print(x, y)
        gcd = euclid(abs(y - x), n)
        #print('pollard new', x, y, gcd)
        i += 1
        if gcd != 1:
            #print('out!!!!!!!!!!!!!!!!!!!!!!!!')
            return gcd
        if i >10000:
            raise Exception('i>1000 at x={}'.format(x0))

def pollard_floyd(n, m=100):
    #print('pollard run with', n)
    gcd = 1
    for i in range(1, m+1):
        gcd0 = pollard_floyd_one(n, i)
        if not is_it_prime(gcd0):
            gcd0 = pollard_floyd(gcd0, m=100)
        elif gcd0 > gcd:
            gcd = gcd0
    return gcd
        
    
if __name__ == '__main__':
    compare(11*12*13*14*15*15*17*18, pollard_floyd, fermat, factorisation, direct)
        
