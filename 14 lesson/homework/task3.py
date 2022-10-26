"""
Дан список словарей, в каждом из словарей есть ключ name и position, он отвечает за расположение элемента в списке.
Position всегда должен быть последовательным, например у нас есть список
data = [
{'name': 'Test 1', 'position': 1},
{'name': 'Test 2', 'position': 2},
{'name': 'Test 3', 'position': 3},
]
Поменять элементы местами, например position 1 и position 3, то должны получить следующий список:
data = [
{'name': 'Test 3', 'position': 1},
{'name': 'Test 2', 'position': 2},
{'name': 'Test 1', 'position': 3},
]
"""

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3}
]
pos1 = int(input('Enter position 1: '))
pos2 = int(input('Enter position 2: '))


def replace_func(pos1: int, pos2: int, data: list):
    if pos1 != pos2 and 0 < pos1 <= len(data) and 0 < pos2 <= len(data):
        data[pos1-1]['name'], data[pos2-1]['name'] = data[pos2-1]['name'], data[pos1-1]['name']
        return data
    else:
        print('\nWrong positions')
        return data


print(replace_func(pos1, pos2, data))
