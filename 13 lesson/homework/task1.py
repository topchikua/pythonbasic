"""
Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента.
"""


lst = [1, 2, 3, 4, 9]
def change(lst):
    first = lst[0]
    last = lst[-1]
    lst[-1] = first
    lst[0] = last
    return lst

print(change(lst))




