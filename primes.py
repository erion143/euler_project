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

def more_prime_numbers(n=1):
    primes = get_primes()
    print(len(primes))
    number = get_number_of_line() * 100 + 1
    print(number)
    for_write = []
    with open(FN, 'a') as out:
        for i in range(n):
            for j in range(50):
                for k in primes:
                    if number % k == 0:
                        break
                else:
                    primes.append(number)
                    for_write.append(number)
                number += 2
            for num in for_write:
                out.write('{}\t'.format(num))
            out.write('\n')
            for_write = []
    return len(primes)     

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

def get_number_of_line():
    with open(FN, 'r') as out:
        lines = out.readlines()
        return len(lines)

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

def get_number(n):
    nums = get_primes()
    if len(nums) < n:
        raise ValueError('Has only {} numbers'.format(len(nums)))
    else:
        print('Has {} numbers.'.format(len(nums)))
        print('{} number is {}.'.format(n, nums[n-1]))
        return nums[n-1]

def sum_of_num_less_n(n):
    with open(FN, 'r') as out:
        res = 0
        for i in out.readlines()[:n//100+1]:
            line = [j.strip() for j in i.split('\t')]
            line = [int(j) for j in line if j]
            res += sum([j for j in line if j <= n])
    return res
    

if __name__ == '__main__':
    compare(2000000, sum_of_num_less_n)
