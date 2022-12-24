from random import randint
n = int(input('Введите количесво чисел: '))
m = [randint(0, 99) for i in range(n)]
print(m)

def sort(array):
    for i in range(1, len(array)):
        z = array[i]
        while i > 0 and array[i - 1] > z:
            array[i] = array[i-1]
            i = i-1
        array[i] = z
    print(array)


sort(m)


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


print('Индекс данного числа: ', binary_search(m, int(input('Какое число нужно найти: '))))

graph = {'0': set(['1', '2']), '1': set(['0', '3', '4']), '2': set(['0']),
         '3': set(['1']), '4': set(['2', '3'])}

def bfs(graph, v):
    visited = {v}
    to_explore = [v]
    while to_explore:
        u = to_explore.pop(0)
        print(u)
        new_vertices = [i for i in graph[u] if i not in visited]
        to_explore.extend(new_vertices)
        visited.update(new_vertices)

bfs(graph, '4')