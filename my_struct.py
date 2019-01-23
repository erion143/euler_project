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


if __name__ == '__main__':
    a = Foo([2,3,5,7])
    b = Foo([3,3])
    print(a + b +b +b +b +b)
    print(b + a)
    print(a - b)
    print(b - a)
        
