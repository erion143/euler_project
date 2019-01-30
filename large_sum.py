from compare import compare

'''
Work out the first ten digits of the sum
of the one-hundred 50-digit numbers in the large_sum.txt
'''

FN = 'large_sum.txt'

def reader():
    with open(FN, 'r') as file:
        ret = []
        for i in file.readlines():
            raw = i.strip() # можно использовать только первые 12-13 цифр
                            # хз сколько точно.
            if raw:
                ret.append(int(raw))
    return ret

def direct(n):
    s = sum(reader())
    return str(s)[:n]

if __name__ == '__main__':
    compare(10, direct)
    
