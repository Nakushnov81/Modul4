from random import randint
n = int(input('Введите количесво чисел: '))
m = sorted([randint(0, 99) for i in range(n)])
print(m)

def binary_search(array, key):
    low = 0
    upp = len(array) - 1
    while low <= upp:
        mid = (low + upp) // 2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            upp = mid - 1
        elif array[mid] < key:
            low = mid + 1
    return 'Такого числа нет в списке'

print(binary_search(m, int(input('Какое число нужно найти: '))))