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

def fermat(n):
    s = roundup(sqrt(n)) ** 2
    while True:
        y = (s + 1) ** 2 - n
        sqy = sqrt(y)
        if sqy == int(sqy):
            print(s+1-sqy, s+1+sqy)
            break
        else:
            s += 1
        if s >= n:
            print('something has gone wrong')
            break
        

if __name__ == '__main__':
    compare(4031, fermat)
    
        
