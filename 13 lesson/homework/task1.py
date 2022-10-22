from random import randint

"""
Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента.
"""

def change(lst):
    first = lst[0]
    last = lst[-1]
    lst[-1] = first
    lst[0] = last
    return lst

lst = [randint(-10, 10) for i in range(randint(2, 7))]

print(f'Исходный список:\n{lst}')
print(f'Список после модификации:\n{change(lst)}')
