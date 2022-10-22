"""
Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
"""


def sum_range(start: int, end: int):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


print(f'\nCумма всех целых чисел = {sum_range(1, 5)}')
