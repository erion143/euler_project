from compare import compare

'''
By considering the terms in the Fibonacci sequence
whose values do not exceed four million,
find the sum of the even-valued terms.
'''

def not_so_direct(n):
    # учитывает, что четным является каждый третий член последовательности Ф.
    # т.о. исключаем одну операцию нахождения остатка от деления,
    # добавляя одно сравнение и одно сложение.
    # В примитивном тесте дает выигрыш примерно в два раза.
    fir = 1
    sec = 1
    count = 3 # Так как вычисляем сразу третье число Ф.
    s = 0
    for i in range(n):
        fir, sec = sec, fir + sec
        if sec >= n: # Проверяем, меньше ли n
            break
        if count == 3: # Проверяем четность, четный каждый 3-й член последов.
            s += sec
            count = 1
        else:
            count += 1
    return s

def direct(n):
    # Не удалось найти формулы для количества чисел Ф., меньших n.
    # Потому кождую итерацию делается проверка. Использование заведомо
    # большего n для инициализации итератора не должно
    # оказать влияния на скорость.

    fir = 1 
    sec = 1 # Оба нечетные
    s = 0
    for i in range(n):
        fir, sec = sec, fir + sec
        if sec >= n: # Проверяем, меньше ли n
            break
        if sec % 2 == 0: # Проверяем четность
            s += sec
    return s   

if __name__ == '__main__':
    compare(2**100000, direct, not_so_direct, pprint=False)
