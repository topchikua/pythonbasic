import string

"""
Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля и выводит свой результат в оценочной шкале от 1 до 5.
1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре
3- у пользователя в пароле соблюдается два условия из (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
4. у пользователя в пароле соблюдается три условия из (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов
"""

pswrd = input('Введите пароль: ')
symbol_count = len(pswrd) > 8
pass_wrong = ['Qwerty123', 'admin', 'password', '123456789', 'qwerty', '']
test = [False, False, False, False]
pass_complexity = 0
for symbol in pswrd:
    if symbol.isdigit():
        test.pop(0)
        test.insert(0, True)
    elif symbol.islower():
        test.pop(1)
        test.insert(1, True)
    elif symbol.isupper():
        test.pop(2)
        test.insert(2, True)
    elif string.punctuation.find(symbol):
        test.pop(3)
        test.insert(3, True)
    else:
        ...
if pass_wrong.count(pswrd) > 0:
    pass_complexity = 1
elif symbol_count and test.count(True) == 4:
    pass_complexity = 5
elif test.count(True) == 3:
    pass_complexity = 4
elif test.count(True) == 2:
    pass_complexity = 3
elif test.count(True) == 1:
    pass_complexity = 2
else:
    ...
print(f'\nНадежность вашего пароля: {pass_complexity}')
