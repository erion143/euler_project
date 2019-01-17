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

def fermat(n, factors = []):
    y = sqrt(n)
    if y == int(y):
        return (int(y), )
    print('run', n)
    s = roundup(sqrt(n))
    k = 0
    while True:
        yy = (s + k) ** 2 - n
        y = sqrt(yy)
        print(k, yy, y)
        if y == int(y):
            if s + k - y == 1:
                return (int(s + k + y), )
            else:
                return fermat(s + k + y) + fermat(s + k - y)
        else:
            k += 0.5
        if k >= n:
            print('something has gone wrong')
            break

        #if i > 30: break
        

if __name__ == '__main__':
    compare(22, factorisation, fermat)
    
        
