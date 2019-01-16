from compare import compare
from time import time

'''
Problem 3
What is the largest prime factor of the number 600851475143 ?
'''

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

if __name__ == '__main__':
    t = time()
    p = prime_numbers(1000000)
    dt = time() - t
    print('time:', dt)
    print(p[-5:])
    
        
