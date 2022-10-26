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