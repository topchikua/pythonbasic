from random import randint

"""
Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента.
"""


def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


lst = [randint(-10, 10) for i in range(randint(2, 7))]

print(f'\nИсходный список:\n{lst}')
print(f'\nСписок после модификации:\n{change(lst)}')
