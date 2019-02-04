from compare import compare

'''
016
What is the sum of the digits of the number 2^1000?
'''

def direct(n):
    return sum(int(i) for i in str(2 ** n))

if __name__ == '__main__':
    compare(1000, direct)
