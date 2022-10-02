"""
Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля и выводит свой результат в оценочной шкале от 1 до 5.
1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре
3 - у пользователя есть буквы в (нижнем или верхнем регистре) и цифры
4 - у пользователя есть цифры, буквы нижнего и верхнего регистра
5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов
"""

pswrd = input('Введите пароль: ')
symbol_lower = False
symbol_upper = False
symbol_digit = False
symbol_count = False
symbol_punctuation = False
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
for symbol in pswrd:
    if symbol.isdigit():
        symbol_digit = True
    elif symbol.islower():
        symbol_lower = True
    elif symbol.isupper():
        symbol_upper = True
    elif symbol.isdigit():
        symbol_digit = True
    elif punctuation.find(symbol):
        symbol_punctuation = True
    else:
         ...
if pswrd == '' or pswrd == 'qwerty' or pswrd == 'admin':
    acces_level = 1
elif symbol_upper and symbol_lower and symbol_digit and symbol_punctuation\
        and len(pswrd) > 8:
    acces_level = 5
elif symbol_upper and symbol_lower and symbol_digit:
    acces_level = 4
elif (symbol_upper or symbol_lower) and symbol_digit:
    acces_level = 3
elif symbol_digit or symbol_lower or symbol_upper or symbol_punctuation:
    acces_level = 2

print(f'\nНадежность вашего пароля: {acces_level}')

