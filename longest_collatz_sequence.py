from compare import compare
from primeFactor import factorisation

'''
#014

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Which starting number, under one million, produces the longest chain?
'''

def next_collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def length_of_chain(n, store={}):
    res = 0
    while n > 1:
        res += 1
        n = next_collatz(n)
    return res

def wrapper(f):
    def inner(n):
        mmax = (1, 1)
        store = {}
        for i in range(1, n+1):
            foo = f(i, store)
            if foo > mmax[1]:
                mmax = (i, foo)
            #if not i % 5000:
                #print(i, mmax)
        return i, mmax
    return inner

def alt_length(n, store):
    res = 0
    temp_store = {n: 0}
    while n > 1:
        res += 1
        n = next_collatz(n)
        if not n in store:
            temp_store[n] = res
        else:
            for i in temp_store:
                store[i] = (res - temp_store[i]) + store[n]
            break
    else:
        for i in temp_store:
            store[i] = res - temp_store[i]
    return res + store[n]

def test(f):
    def inner(n):
        store = {}
        for i in range(1, n):
            print(i, f(i, store=store))
    return inner
            
direct = wrapper(length_of_chain)
not_so_direct = wrapper(alt_length)

if __name__ == '__main__':
   compare(5000000, not_so_direct)
