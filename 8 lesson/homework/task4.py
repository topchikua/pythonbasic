import random
import string

"""
Напишите программу где пользователь вводит число symbol_len, а программа генерирует пароль длинной symbol_len.
Чем выше будет сложность пароля, тем лучше. Сложность пароля буду оценивать по шкале от 1 до 5 из задании #3
"""

symbol_types = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
temp = symbol_types.copy()
symbol_len = int(input('\nУкажите длину пароля = '))
password = []
if symbol_len > 0:
    for i in range(symbol_len):
        if i <= 3:
            symbol = random.choices(temp)
            password += ''.join(random.choices(symbol[0]))
            temp.pop(temp.index(symbol[0]))
        elif i >= 4:
            symbol = random.choices(symbol_types)
            password += ''.join(random.choices(symbol[0]))
            random.shuffle(password)
else:
    print('Ошибка. Количество символов пароля не может быть меньше 1')
    exit()
password = ''.join(password)
print(f'\nВаш пароль: {password}')
