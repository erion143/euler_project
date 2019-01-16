from compare import compare

'''
The simplest task from Euler Project
It is need to find summ of every numbers wich are divided by 3 or 5
and less than 1000
'''

def direct(n):
    # the simplest brute force solution
    s = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s

def not_so_direct(n):
    # passage through the numbers wich are divided by 3 or 5
    s = 0
    current_number = 0
    counter = 0
    n1 = n-3
    n2 = n-5
    while current_number < n1:
        current_number += 3
        s += current_number
    current_number = 0
    while current_number < n2:
        current_number += 5
        # elimination of duplications
        counter += 1
        if counter == 3:
            counter = 0
            continue
        s += current_number
    return s

def not_so_direct_with_tiny_opt(n):
    # modification of previous algorithm with use for cicle instead of while
    s = 0
    current_number = 0
    counter = 0
    # amount ot the numbers wich are divided by 3 and less than n
    n1 = (n-1)//3
    # amount ot the numbers wich are divided by 5 and less than n
    n2 = (n-1)//5
    for i in range(n1):
        current_number += 3
        #print(current_number, end=', ')
        s += current_number
    current_number = 0
    for i in range(n2):
        current_number += 5
        # elimination of duplications
        counter += 1
        if counter == 3:
            counter = 0
            continue
        #print(current_number, end=', ')
        s += current_number
    return s

def not_so_direct_with_another_tiny_opt(n):
    current_number = 0
    counter = 0
    n1 = (n-1)//3
    n2 = (n-1)//5
    s = sum(range(1, n1+1)) * 3
    current_number = 0
    for i in range(n2):
        current_number += 5
        counter += 1
        if counter == 3:
            counter = 0
            continue
        #print(current_number, end=', ')
        s += current_number
    return s

def not_so_direct_with_another_once_tiny_opt(n):
    current_number = 0
    counter = 0
    n1 = (n-1)//3
    n2 = (n-1)//5
    s = sum(range(1, n1+1)) * 3
    q = (i for i in range(1, n2+1) if i % 3 != 0)
    s += (sum(q) * 5)
    return s

if __name__ == '__main__':
   compare(1000,
           direct,
           not_so_direct,
           not_so_direct_with_tiny_opt,
           not_so_direct_with_another_tiny_opt,
           not_so_direct_with_another_once_tiny_opt)
