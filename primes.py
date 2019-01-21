from compare import compare
from math import sqrt

FN = 'primes.txt'

def prime_numbers(max_n):
    prime = [2,3]
    number = 5
    j = 1
    while True:
        if j == 3:
            j = 1
            continue
        else:
            j += 1
        for i in prime:
            if number % i == 0:
                break
        else:
            prime.append(number)
        number += 2
        if number > max_n:
            return prime[-1]

def prime_numbers_old(max_n):
    with open(FN, 'w') as out:
        prime = [2,3]
        number = 5
        j = 1
        for_write = [2,3]
        for j in range(48):
            for i in prime:
                if number % i == 0:
                    break
            else:
                prime.append(number)
                for_write.append(number)
            number += 2
        for num in for_write:
            out.write('{}\t'.format(num))
        out.write('\n')
        for_write = []
        while True:
            for j in range(50):
                for i in prime:
                    if number % i == 0:
                        break
                else:
                    prime.append(number)
                    for_write.append(number)
                number += 2
            for num in for_write:
                out.write('{}\t'.format(num))
            out.write('\n')
            for_write = []
            if number > max_n:
                return prime[-1]

def is_it_prime(n):
    if n == 1: return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if i == 139:
            print(n / 139)
        if n % i == 0:
            return False
    else:
        return True

if __name__ == '__main__':
    compare(1000000, prime_numbers_old)
