"""
Задание 4:
Вывести на экран таблицу умножения от 1 до 10 с помощью двух циклов for.
"""

x = 1
y = 10
print(f'\nТаблица умножения от {x} до {y}:\n')
for i in range(x, y + 1):
    for j in range(x, y + 1):
        print(i * j, end='\t')
    print()
