import json


# C = {'key': [1, 'Hello'], 'key2': True}
#
# print(json.dumps(C))
#
# f = open('data.json', 'w')
# print(json.dump(C, f))


# for i in range(3):
#     stop = False
#     for j in range(10):
#         if j == 8:
#             stop = True
#             break
#     if stop:
#         break


# a = [1, 2, 3, 4]

# b = []
# for i in a:
#     b.append(str(i))

# b = list(map(str, a))

# result = '-'.join(a)
# print(result)
# print('start')
# try:
#     a = int(input('Enter number: '))
#     print(a)
# except ValueError as e:
#     print(f'Error! {e}\n Введите число!')
# print('End')
# print(int('b'))

# try:
#     a = int(input('Enter number: '))
#     b = int(input('Enter number: '))
#     # [][0]
#     print(a / b)
# except (ValueError, ArithmeticError) as e:
#     print(f'Error! {e} Введите число!')
# # except Exception as e:
# #     print(f'Exception Error: {e}')
# else:
#     print('No Error')
#     print(f'Value {a}')
# finally:
#     print('finally')


# while True:
#     try:
#         a = int(input('Enter number: '))
#
#         if a == 10:
#             raise ValueError('number == 10')
#         if a == -1:
#             break
#         print(a)
#     except Exception as e:
#         print(f'Error: {e}')


# word_index = 'Hello world'.find('Hello')
# str_len = len('Hello world')


# def greetings():
#     print(((5 * '*') + '\n') * 5)
#     print('----')
#
#
# greetings()
# greetings()
# greetings()
# greetings()
# greetings()
# greetings()
# greetings()
# greetings()
# greetings()

# a = int(input('Number #1: '))  # 4
# b = int(input('Number #2: '))  # 2

# def get_max_number(a, b):
#     if a > b:
#         print(f'Max number is A = {a}')
#     else:
#         print(f'Max number is B = {b}')


# def get_max_number(a, b=10):
#     if a > b:
#         return a, 'A'
#     else:
#         return b, 'B'
#
#
# number, name = get_max_number(-10, 2)
# print(f'number = {number} & name = {name}')
# number, name = get_max_number(-10, 2)
# print(f'number = {number} & name = {name}')
# print('get_max_number', get_max_number(10, 2))
# import copy
#
#
# def foo(a):
#     a = copy.deepcopy(a)
#     a += [1]
#     return a
#
#
# list_a = [1, 2, 3]
# print(list_a)
# foo(list_a)
# print(list_a)
#


def foo(n, a=None):
    if a is None:
        a = []
    for i in range(n):
        a.append(i)
    return a

# print(foo(5, ['asd', 123,54]))
# c = foo(2)
# d = foo(4)
# e = foo(10)
#
# print(hex(id(c)))
# print(hex(id(d)))
# print(hex(id(e)))

# *a, i, *b = [1, 2, 3, 4]
# print(a, i, b)


# def get_max_number(n, *numbers, **additional_fields):
#     max_number = numbers[0]
#     for number in numbers:
#         if max_number < number:
#             max_number = number
#     return max_number
#
#
# print(get_max_number(1, 2, 3, 4, 5, key_1=123123, key_2='Hello world'))

from typing import Union, List, Optional

import requests


def get_number(n: int) -> Optional[int]:
    if n > 10:
        return n


def get_max_number(a: int, b: int) -> List[Union[int, str]]:
    """
    Функция get_max_number принимает два числа и возвращает список внутри которого может быть int, str
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('a и b должны быть целыми числами')

    if a > b:
        return [a, 'A']
    else:
        return [b, 'A']


value = get_max_number(10.5, 4)
print(value[1])