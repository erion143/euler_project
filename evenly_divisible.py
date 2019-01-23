from primes import get_primes
from my_struct import Foo
from compare import compare
from primeFactor import factorisation

'''
005
What is the smallest positive number
that is evenly divisible by all of the numbers from 1 to 20?
'''

def direct(n):
    p = get_primes(last=n)
    mmin = 1
    for i in p:
        mmin *= i
    while True:
        for i in range(1, n+1):
            if mmin % i != 0:
                mmin += 1
                break
        else:
            return mmin

def not_so_direct(n):
    # разложим каждый потенциальный делитель на простые множители
    # Пусть есть множество A {ni Ki}, содержащее ni элементов Ki
    # Определим операцию :: над множеством А
    # A1 {ni Ki} :: A2 {mi Ki} = A3 {max(ni, mi) Ki}
    # тогда наименьшим положительным целым числом, нацело делящиимся
    # на все числа от 1 до n можно выразить как произведение всех элементов 
    # множества А, которое:
    # A = {} :: A1 :: A2 :: A3 :: ... :: A(n-1) :: An,
    # где Ai - множество простых делителей числа i, n - положительное целое
    # число, на числа вплоть до которого должен нацело делиться езультат
    prime_factors = []
    for i in range(2, n+1):
        prime_factors.append(Foo(factorisation(i, factors=[])))
    res = Foo()
    for foo in prime_factors:
        res = res + foo
    return res.self_product()
    
if __name__ == '__main__':
    compare(10000, not_so_direct)
