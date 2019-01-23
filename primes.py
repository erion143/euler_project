from compare import compare
from math import sqrt

FN = 'primes.txt'

def prime_numbers(max_n):
    # не очень удачная реализация вычислялки простых чисел
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
    # более "наивная" реализация, но работает быстрее
    with open(FN, 'w') as out:
        prime = [2,3]
        number = 5
        j = 1
        for_write = [2,3]
        # -- Вычисление простых чисел в инервале [1,100] -------
        for j in range(48):
            for i in prime:
                if number % i == 0:
                    break
            else:
                prime.append(number)
                for_write.append(number)
            number += 2
        # их запись
        for num in for_write:
            out.write('{}\t'.format(num))
        out.write('\n')
        # ------------------------------------------------------
        for_write = []
        # -- Вычисление простых чисел в инервале [101,max_n] ---
        while True:
            # Вычисление ведется в каждой сотне чисел поочереди
            for j in range(50):
                for i in prime:
                    if number % i == 0:
                        break
                else:
                    prime.append(number)
                    for_write.append(number)
                number += 2
            # запись результата после перебора очередной сотни чисел
            for num in for_write:
                out.write('{}\t'.format(num))
            out.write('\n')
            for_write = []
            # если достигли max_n заканчиваем выполнение
            if number > max_n:
                return prime[-1]

def is_it_prime(n):
    if n == 1: return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    else:
        return True

def read_one_line(s):
    ret = [i.strip() for i in s.split('\t')]
    ret = [int(i) for i in ret if i] 
    return ret

def _get_primes(start=0, stop=0):
    ret = []
    with open(FN, 'r') as out:
        lines = out.readlines()
        full = len(lines)
        if stop > full:
            raise ValueError('Where is not {} lines'.format(stop))
        if stop:
            for line in lines[start:stop]:
                ret += read_one_line(line)
        else:
            for line in lines[start:]:
                ret += read_one_line(line)
    return ret

def get_primes(first=0, last=0):
    if first and last:
        f = (lambda x: (x >= first) and (x <= last))
        start = first // 100
        stop = last // 100 + 1
    elif first:
        start = first // 100
        f = (lambda x: x >= first)
        stop = 0
    elif last:
        stop = last // 100 + 1
        f = (lambda x: x <= last)
        start = 0
    else:
        stop = 0
        start = 0
        f = (lambda x: True)
    ret = _get_primes(start=start, stop=stop)
    return [i for i in ret if f(i)]
    

if __name__ == '__main__':
    print(get_primes(first=10, last=150))
