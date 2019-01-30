from compare import compare
from primeFactor import factorisation
from my_struct import Binar
from auxilary import product # перемножает элементы списка

'''
What is the value of the first triangle number
to have over five hundred divisors?
'''

# Треугольные числа:
# a[0] = 0
# a[i] = a[i-1] + i

def triangle_number(n):
    return sum(range(1, n+1))

def divisors(n):
    # Находим все делители прямым перебором
    ret = []
    for i in range(1, n+1):
        if n % i == 0:
            ret.append(i)
    return ret

def direct(n):
    # Используем функцию divisors для поиска делителей
    # Работает ОЧЕНЬ медленно
    cur = triangle = 0
    mmax = (0, 0) # Тут храним число с максимумом делителей
                  # и число его делителей
    while True:
        cur += 1  # Фактическии, номер треугольного числа
        triangle += cur # Само треугольное число
        #print(triangle)
        div = divisors(triangle) # Список делителей
        #print(div)
        if len(div) >= mmax[1]:  # Если он длиннее предыдущего максимума
            mmax = (triangle, len(div)) # Записываем новый максимум
            if mmax[1] >= n:                  # Если число делителей больше
                return triangle, cur, mmax[1] # заданного - ответ найден
        if not cur % 1000:  # Каждую 1000 перебранных чисел печатаем максимум
            print(cur, triangle, mmax) # чтоб не скучно было.

def combinations(n):
    # Генерируем список всех делителей числа n
    l = factorisation(n, factors=[]) # Список простых множителей числа n
    #print(l)
    b = Binar(len(l)) # Вспомогательный объект, в основе которого
                      # двоичное предстваление числа
    length = 2 ** len(l) - 1 # Число комбинаций чисел из списка l,
                             # не считая пустой комбинации
    res = set((1,)) # Так как простые множители могут повторяться,
                    # среди комбинаций тоже будут одинаковые.
                    # Автоматически фильтруем повторы, используя SET
                    # для хранения делителей (произведений комбинаций
                    # простых множителей).
    for i in range(length):
        b.next()
        # b.accept(l) - число на позиции i вносится в список, если на
        # позиции i в двоичном представлении номера итерации стоит 1.
        res.add(product(b.accept(l)))
    #print(res)
    return res

def not_so_direct(n):
    # Используем функцию combinations для поиска делителей
    # В остальном идентична direct
    # Работает существенно быстрее direct
    cur = triangle = 0
    mmax = (0, 0)
    while True:
        cur += 1
        triangle += cur
        #print(triangle)
        div = combinations(triangle)
        if len(div) >= mmax[1]:
            mmax = (triangle, len(div))
            if mmax[1] >= n:
                return triangle, cur, mmax[1]
        if not cur % 1000:
            print(cur, triangle, mmax)

if __name__ == '__main__':
    compare(1000, not_so_direct)
