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