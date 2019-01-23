from compare import compare

'''
006
Find the difference between the sum of the squares
of the first one hundred natural numbers
and the square of the sum.
'''

def direct(n):
    # Прямой метод будкт оптимален по скорости
    sum_of_squares = sum(i ** 2 for i in range(1, n+1))
    square_of_sum = sum(i for i in range(1, n+1)) ** 2
    return square_of_sum - sum_of_squares

def not_so_direct(n):
    ret = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            ret += 2 * i * j
    return ret

if __name__ == '__main__':
    compare(20000, direct, not_so_direct)
