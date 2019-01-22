from random import randint
from compare import compare
from primeFactor import factorisation

'''
# 003
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(n):
    sn = str(n)
    if sn == sn[::-1]:
        return True
    else:
        return False


def is_palindrome1(n):
    '''
    Работает медленнее, чем is_palindrome
    '''
    l = []
    while n:
        l.append(n % 10)
        n = n // 10
    if l == l[::-1]:
        return True
    else:
        return False

def test_generator(n):
    test = []
    for i in range(n):
        test.append(randint(9999, 999999))
    return test

def iterator(f):
    def inner(l):
        out = []
        for i in l:
            out.append(f(i))
        return any(out)
    return inner

def direct(n):
    res = []
    for i in range(10**(n-1), 10**n):
        for j in range(i, 10**n):
            p = i * j
            if is_palindrome(p):
                res.append((p, i, j))
    return max(res, key=(lambda x: x[0]))

def to_n_digit(l): pass


if __name__ == '__main__':
    compare([3, 11, 83, 331], to_n_digits)
