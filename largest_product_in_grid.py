from random import randint
from compare import compare

FN = 'sample.txt'

def generate(n):
    with open(FN, 'w') as out:
        for i in range(n):
            for j in range(n):
                out.write(str(randint(0, 99)).zfill(2))
                out.write(' ')
            out.write('\n')

def read():
    with open(FN, 'r') as out:
        data = out.read()
    return data

class Matrix:
    def __init__(self, s):
        data = s.split('\n')
        data = [i for i in data if i]
        self.h = len(data)

        data = [[int(j) for j in i.split(' ') if j] for i in data]
        self.w = len(data[0])

        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __repr__(self):
        ret = ''
        for i in range(self.h):
            for j in range(self.w):
                ret = ret + '{} '.format(str(self[i][j]).zfill(2))
            ret += '\n'
        return ret

    def gen_S(self, i, j):
        if (i + 4) > self.h:
            #print('{} >= {}'.format((i + 4), self.h))
            return ()
        return (self[k][j] for k in range(i, i+4))

    def gen_E(self, i, j):
        if (j + 4) > self.w:
            return ()
        return (self[i][k] for k in range(j, j+4))

    def gen_SE(self, i, j):
        if (i + 4) > self.h or (j + 4) > self.w:
            return ()
        return (self[ii][jj] for ii, jj in zip(range(i, i+4),
                                               range(j, j+4)))

    def gen_SW(self, i, j):
        if (i + 4) > self.h or (j - 3) < 0:
            return ()
        return (self[ii][jj] for ii, jj in zip(range(i, i+4),
                                               range(j, j-4, -1)))

def prod(it):
    res = 1
    for i in it:
        res *= i
    return res

def direct(s):
    m = Matrix(s)
    res = 1
    foo = ()
    for i in range(m.h):
        for j in range(m.w):
            for f in (m.gen_E, m.gen_S, m.gen_SE, m.gen_SW):
                #res = max(res, prod(f(i, j)))

                bar = tuple(f(i, j))
                #print(i, j, bar, prod(bar))
                if prod(bar) > res:
                    foo = bar
                    res = prod(bar)
    print(foo)
    return res
                    
        
if __name__ == '__main__':
    #generate(5)
    mm = Matrix(read())
    print(mm)
    compare(read(), direct)
