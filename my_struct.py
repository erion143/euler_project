import collections.abc

INF = 10^10

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

class BinaryCounter(collections.abc.Iterator):
    def __init__(self, n):
        self.dim = n
        self.obj = []
        self.reset()

    def reset(self):
        # В конце списка - так как приходится делать проход перед возвратом
        # результата, а пустое множество тоже нужно вернуть.
        self.obj = [0 for i in range(self.dim-1)] + [-1]

    def __next__(self):
        for i in range(self.dim-1, -1, -1):
            if self.obj[i] == 0 or self.obj[i] == -1:
                self.obj[i] += 1
                break
            else:
                self.obj[i] = 0
        else:
            raise StopIteration
        return self.obj

    def __repr__(self):
        return 'BINAR {}'.format(self.obj)

    @staticmethod
    def accept(obj, other):
        return [i for i, j in zip(other, obj) if j]


class Vertex:
    def __init__(self, graph):
        self.prop = 0
        self.edges = {}
        self.graph = graph
        self.ind = graph.add(self)

    def add_edge(self, other, w=1):
        self.edges[other.ind] = w

    def __eq__(self, other):
        return self.prop == other.prop

    def __gt__(self, other):
        return self.prop > other.prop

    def __lt__(self, other):
        return self.prop < other.prop

class Graph:
    def __init__(self):
        self.verteces = []
        next_ind = 0

    def add(self, vertex):
        self.verteces.append(vertex)
        next_int += 1
        return next_ind - 1

    def add_single_edge(v1, v2):
        assert v1 in self.verteces and v2 in self.verteces
        v1.add_edge(v2)

    def add_edge(v1, v2):
        assert v1 in self.verteces and v2 in self.verteces
        v1.add_edge(v2)
        v2.add_edge(v1)

class Dijkstra(Graph):
    def __init__(self):
        Graph.__init__(self)
        self.queue = set()
        self.gone = []
        for i in self.verteces:
            i.prop = INF

    def __call__(self, vertex):
        assert vertex in self.verteces
        vertex.prop = 0
        self.queue.append(vertex)
        while self.queue:
            self.test(min(self.queue))
            self.gone.append(min(self.queue))

    def test(self, vertex):
        for i in vertex.edges:
            if self.verteces[i] in self.gone:
                continue
            prop = vertex.prop + vertex.edges[i]
            if self.verteces[i].prop > prop:
                self.verteces[i].prop = prop
            self.queue.add(self.verteces[i])
            

if __name__ == '__main__':
    b = BinaryCounter(4)
    for i in b:
        print(i)
        
