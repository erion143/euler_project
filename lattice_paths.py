from compare import compare
from auxilary import factorial as fact

'''
015
Starting in the top left corner of a 20×20 grid,
and only being able to move to the right and down,
how many such routes are there through a 20×20 grid?
'''

# Какой бы маршрут не был выбран - по сетке n * m потребуется совершить
# m шагов по горизонтали и n шагов по вертикали.
# Допустимо любое сочетание таких количеств шагов
# Общее количество сочетаний будет определяться формулой
# (m + n)! / m! / n!

def direct(n):
    #Для квадратной сетки
    return fact(2 * n) / fact(n) / fact(n)

if __name__ == '__main__':
    compare(20, direct)
