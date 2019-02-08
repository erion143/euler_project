from compare import compare
from number_letter_counts_dict import data, data_num

'''
If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

def reader(n):
    res = {}
    for i in range(n):
        a = n % 10
        if a:
            res[10 ** i] = a
        n //= 10
        if not n:
            return res
        
def to_words(n):
    ret = ''
    res = reader(n)
    if 100 in res:
        ret += '{} {}'.format(data[res[100]], data[100])
        if 10 in res or 1 in res:
            ret += ' and '
    if 10 in res:
        if res[10] == 1:
            ret += data[res[10] * 10 + res.get(1, 0)]
            return ret
        else:
            ret += data[res[10]*10]
            if res.get(1, 0):
                ret += '-'
    if 1 in res:
        ret += data[res[1]]
    return ret

def lin_direct(n):
    nw = to_words(n)
    nw = nw.replace(' ', '').replace('-', '')
    return len(nw)

def lin_not_direct(n):
    res = reader(n)
    ret = 0
    if 100 in res:
        ret += (data_num[100] + data_num[res[100]])
        if 10 in res or 1 in res:
            ret += 3
    if 10 in res:
        if res[10] == 1:
            ret += data_num[10 + res.get(1, 0)]
            return ret
        else:
            ret += data_num[10 * res[10]]
    if 1 in res:
        ret += data_num[res[1]]
    return ret

def wrapper_direct(f):
    def inner(n):
        result = 0
        for i in range(1, n):
            result += f(i)
        return result
    return inner

def hz(n):        
    # n неважно. Счет до 999 включительно
    sum1 = sum(data_num[i] for i in range(1, 10))
    sum2 = sum(data_num[i] for i in range(10, 20))
    sum3 = sum(data_num[i] for i in range(20, 100, 10))
    other1 = data_num[100]
    other2 = len('and')
    #other3 = len('one thousand') - 1

    result = (other1 * 900 + # 9 раз по 100 раз слово hundred 
              other2 * 891 + # 9 раз по 100 раз - 9
              #other3 +
              sum1 * (100 + 10 * 9) + # 9 раз в каждой сотне
                                      # + 100 раз в своей сотне
              sum2 * 10 + # один раз в каждой сотне
              sum3 * 10 * 10) # десять раз в каждой сотне

    return result

direct = wrapper_direct(lin_direct)
direct.__name__ = 'direct'
not_so_direct = wrapper_direct(lin_not_direct)
not_so_direct.__name__ = 'not_so_direct'

if __name__ == '__main__':
    compare(1000, direct, not_so_direct, hz)
