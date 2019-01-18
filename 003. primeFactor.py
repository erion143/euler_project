from compare import compare
from time import time
from math import sqrt

'''
Problem 3
What is the largest prime factor of the number 600851475143 ?
'''

def roundup(n):
    return int(n) + (n % 1 > 0)

def prime_numbers(max_n=0):
    prime = [2,3]
    number = 5
    t = time()
    while True:
        for i in prime:
            if number % i == 0:
                break
        else:
            prime.append(number)
        number += 2
        if number > max_n:
            return prime

def factorisation(n, factors=[]):
    for i in range(2, int(n//2)):
        if n % i == 0:
            factors.append(i)
            return factorisation(n // i, factors=factors)
    else:
        return factors + [n]

def is_it_prime(n):
    if n == 1: return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return False
    else:
        return True

def fermat(n, main=True):
    #print('run', n, ':', end=' ')
    if n % 2 == 0:
        return sorted([2, ] + fermat(n / 2, main=False))
    y = sqrt(n)
    if y == int(y):
        if main:
            return sorted(fermat(y, main=False) + fermat(y, main=False))
        else:
            return fermat(y, main=False) + fermat(y, main=False)
    s = roundup(sqrt(n))
    k = 0
    while True:
        yy = (s + k) ** 2 - n
        y = sqrt(yy)
        if y == int(y):
            if s + k - y == 1:
                return [int(s + k + y), ]
            else:
                if main:
                    return sorted(fermat(s + k + y, main=False)
                                  + fermat(s + k - y, main=False))
                else:
                    return (fermat(s + k + y, main=False)
                            + fermat(s + k - y, main=False))
        else:
            k += 1
        if k >= n:
            print('something has gone wrong')
            break        

if __name__ == '__main__':
    compare(817**3*417**2*411, factorisation, fermat)
    
        
