"""
Дан список словарей, в каждом из словарей есть ключ name и position, он отвечает за расположение элемента в списке.
Position всегда должен быть последовательным, например у нас есть список
data = [
{'name': 'Test 1', 'position': 1},
{'name': 'Test 2', 'position': 2},
{'name': 'Test 3', 'position': 3},
]
И мы хотим удалить элемент у которого position = 2, то на выходе мы должны получить следующий список:
data = [
{'name': 'Test 1', 'position': 1},
{'name': 'Test 3', 'position': 2},  # -1
]
"""

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3}
]

pos = int(input('Enter position: '))


def del_func(pos):
    for i in range(len(data)):
        if data[i]['position'] == pos:
            data.pop(i)
            for j in range(len(data)):
                data[j]['position'] = j + 1
            return data
    print('Wrong position!')
    return data


print(del_func(pos))
