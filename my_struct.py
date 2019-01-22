class Foo:
    def __init__(self, obj):
        self.obj = {}
        self.append(obj)

    def __repr__(self):
        return 'foo ' + str(self.obj)

    def get(self):
        ret = []
        for i in self.obj:
            for j in range(self.obj[i]):
                ret.append(i)
        sorted(ret)
        return ret

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


if __name__ == '__main__':
    a = Foo([2,3,5,7])
    b = Foo([3,3])
    print(a.summ(b).get())
        
