"""
1. Написать программу которая проверяет что в строке есть хотя бы один пробел, число, буква нижнего и верхнего регистра.
Если это так, то вывести 'YES', иначе 'NO'
"""

test_string = 'Hello World1'
symbol_detail = [False, False, False, False]
for symbol in test_string:
    if symbol.isspace():
        symbol_detail[0] = True
    elif symbol.islower():
        symbol_detail[1] = True
    elif symbol.isupper():
        symbol_detail[2] = True
    elif symbol.isdigit():
        symbol_detail[3] = True
    else:
        ...
if symbol_detail.count(True) == 4:
    print('\nYES')
else:
    print('\nNO')
