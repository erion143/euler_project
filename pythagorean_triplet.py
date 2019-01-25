from compare import compare

'''
009
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def direct(n):
    out = []
    for a in range(1, n//3):
        for b in range(a, n):
            c = n - a - b
            if c <= b: continue
            if (a ** 2 + b ** 2) == (c ** 2):
                out.append((a, b, c))
    return out

def not_so_direct(n):
    out = []
    def fc(b):
        num = n ** 2 - 2 * n * b + 2 * b ** 2
        denom = 2 * (n - b)
        return num / denom
    for b in range(2, int((n-2)/2)+2):
        c = fc(b)
        if int(c) == c:
            a = n - b - c
            if a < b < c and a ** 2 + b ** 2 == c ** 2:
                out.append((int(a), b, int(c)))
    return out

def not_so_direct_with_tiny_opt(n):
    out = []
    for b in range(2, int((n-2)/2)+2):
        bb = b ** 2
        c = (n ** 2 - 2 * n * b + 2 * bb) / (2 * (n - b))
        ci = int(c)
        if ci == c:
            a = n - b - ci
            if a < b < c and a ** 2 + bb == ci ** 2:
                out.append((a, b, ci))
    return out

def test(f):
    def inner(n):
        out = []
        for i in range(6, n+1):
            ret = f(i)
            if ret:
                out += ret
        return any(out)
    return inner

foo1 = test(direct)
foo2 = test(not_so_direct)
foo3 = test(not_so_direct_with_tiny_opt)
    

if __name__ == '__main__':
    compare(12000, foo2, foo3)
    
        
