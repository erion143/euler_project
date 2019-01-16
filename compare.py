from time import time

def compare(arg, *fs, pprint=True):
    for f in fs:
        if pprint:
            t1 = time()
            print(f(arg))
            t2 = time()
        else:
            t1 = time()
            foo = f(arg)
            t2 = time()
        print(f.__name__, ':', t2-t1, 'sec')
