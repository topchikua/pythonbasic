"""
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines
(на всякий случай проверим, что задано положительное целое число).
"""


def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            text_lines = text.readlines()[-lines:]
        print(f'\nКоличество последних строк строк: {lines}\nФайл: {file}\n')
        for line in text_lines:
            print(line.strip())
    else:
        print('\nКоличество строк указано неверно.\nТолько положительное число!')

read_last(3, 'task4.txt')