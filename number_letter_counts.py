from compare import compare
from number_letter_counts_dict import data

'''
If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

def interpriter(n):
    res = {}
    for i in range(n):
        res[10 ** i] = n % 10
        n //= 10
        if not n:
            break
    ret = ''
    if 100 in res:
        ret += '{} {}'.format(data[res[100]], data[100])
        if 10 in res or 1 in res:
            ret += ' and '
    if 10 in res:
        if res[10] == 1:
            ret += data[res[10] * 10 + res[1]]
            return ret
        else:
            ret += data[res[10]*10]
            if res[1]:
                ret += '-'
    if 1 in res:
        ret += data[res[1]]
    return ret

if __name__ == '__main__':
    compare(115, interpriter)
