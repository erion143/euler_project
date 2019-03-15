from random import randint
from my_struct import BinaryCounter, Dijkstra, Vertex
from compare import compare
from auxilary import flat

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

def triangle_to_linear(x, y):
    return sum(range(1, x+1)) + y

class Bar(Dijkstra):
    def __init__(self, l):
        Dijkstra.__init__(self)
        ll = flat(l)
        v0 = Vertex(self)
        v1 = Vertex(self)
        self.add_single_edge(v0, v1, ll[0])
        
        for i in range(1, len(l)):
            for j in range(len(l[i])):
                Vertex(self)
            for k in range(len(l[i-1])):
                pass
            

if __name__ == '__main__':
    print(triangle_to_linear(3, 2))

