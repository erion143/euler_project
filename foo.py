from random import randint
from my_struct import BinaryCounter
from compare import compare

'''
#018
Find the maximum total from top to bottom of the triangle in empty.txt
'''

FN = 'empty1.txt'

def generator(n):
    with open(FN, 'w') as out:
        for i in range(1, n+1):
            for j in range(i):
                print(str(randint(0, 99)).zfill(2), file=out, end=' ')
            print(file=out)
    
def reader():
    data = []
    with open(FN, 'r') as inn:
        for line in inn.readlines():
            print(line, end='')
            d = [i.strip() for i in line.split(' ')]
            d1 = [int(i) for i in d if i]
            data.append(d1)
    return data

def sum_of_previous(l):
    data = [0]
    for i in l:
        data.append(data[-1] + i)
    return data

def direct(*args):
    # Сложность O(2^n)
    # т.к. количество путей 2 ^(число строк - 1)
    data = reader()
    print()
    mmax = 0
    mpath = []
    b = BinaryCounter(len(data)-1)
    for i in b:
        path = sum_of_previous(b.obj)
        res = 0
        for j, k in zip(data, path):
            res += j[k]
        if res > mmax:
            mmax = res
            mpath = path
    return mmax, mpath

if __name__ == '__main__':
    generator(20)
    compare(1, direct)

