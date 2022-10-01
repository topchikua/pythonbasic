"""
1. Написать программу которая проверяет что в строке есть хотя бы один пробел, число, буква нижнего и верхнего регистра.
Если это так, то вывести 'YES', иначе 'NO'
"""

test_string = 'sndsjd(((    4848484J'
symbol_space = False
symbol_lower = False
symbol_upper = False
symbol_digit = False
for symbol in test_string:
    if symbol.isspace():
        symbol_space = True
    elif symbol.islower():
        symbol_lower = True
    elif symbol.isupper():
        symbol_upper = True
    elif symbol.isdigit():
        symbol_digit = True
    else:
        ...
if symbol_space is True and symbol_lower is True and symbol_upper is True \
        and symbol_digit is True:
    print('\nYES')
else:
    print('\nNO')
