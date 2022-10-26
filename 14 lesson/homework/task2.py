"""
Дан список словарей, в каждом из словарей есть ключ name и position, он отвечает за расположение элемента в списке.
Position всегда должен быть последовательным, например у нас есть список
data = [
{'name': 'Test 1', 'position': 1},
{'name': 'Test 2', 'position': 2},
{'name': 'Test 3', 'position': 3},
]
Добавление элемента с любым position, например мы хотим в наш исходный список добавить элемент у которого position = 1,
то должны получить:
data = [
{'name': 'Test 4', 'position': 1}
{'name': 'Test 1', 'position': 2},  # +1
{'name': 'Test 2', 'position': 3},  # +1
{'name': 'Test 3', 'position': 4},  # +1
]
"""

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3}
]

pos = int(input('Enter position: '))
name = input('Enter name: ')


def add_func(pos: int, name: str, data: list):
    if pos > len(data) + 1:
        pos = len(data) + 1
        print(f'\nИндекс позиции замененен на максимально допустимый: - {len(data) + 1} !!!')
    elif pos <= 0:
        pos = 1
        print(f'\nИндекс позиции замененен на минимально допустимый: {pos} !!!')
    data.insert(pos - 1, {'name': name, 'position': pos})
    for i in range(pos, len(data)):
        if pos <= data[i]['position']:
            data[i]['position'] += 1
    return data


print(add_func(pos, name, data))
