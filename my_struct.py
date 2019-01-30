class Foo:
    def __init__(self, obj=()):
        self.obj = {}
        self.append(obj)

    def __repr__(self):
        return 'foo' + str(self.obj)

    def __add__(self, other):
        return self.summ(other)

    def __sub__(self, other):
        return self.difference(other)

    def __radd__(self, other):
        return other.summ(self)

    def __rsub__(self, other):
        return other.difference(self)

    def get(self):
        ret = []
        for i in self.obj:
            for j in range(self.obj[i]):
                ret.append(i)
        return sorted(ret)

    def append(self, obj):
        for i in obj:
            if not i in self.obj:
                self.obj[i] = 1
            else:
                self.obj[i] += 1

    def difference(self, other):
        result = Foo(self.get())
        for i in other.obj:
            if i in result.obj:
                d = result.obj[i] - other.obj[i]
                if d <= 0:
                    result.obj.pop(i)
                else:
                    result.obj[i] = d
        return result

    def summ(self, other):
        result = other.difference(self)
        result.append(self.get())
        return result

    def self_product(self):
        ret = 1
        for i in self.obj:
            ret *= (i ** self.obj[i])
        return ret

class Binar:
    def __init__(self, n):
        self.dim = n
        self.obj = []
        self.reset()

    def reset(self):
        self.obj = [0 for i in range(self.dim)]

    def next(self):
        for i in range(self.dim-1, -1, -1):
            if self.obj[i] == 0:
                self.obj[i] = 1
                break
            else:
                self.obj[i] = 0
        else:
            raise ValueError('binar object overflow')

    def __repr__(self):
        return 'BINAR {}'.format(self.obj)

    def accept(self, other):
        return [i for i, j in zip(other, self.obj) if j]


if __name__ == '__main__':
    b = Binar(4)
    while 1:
        b.next()
        print(b)
        
