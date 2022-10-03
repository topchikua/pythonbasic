import string

"""
Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля 
и выводит свой результат в оценочной шкале от 1 до 5.
 1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
 2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре
 3 - у пользователя в пароле соблюдается два условия из 
 (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
 4 - у пользователя в пароле соблюдается три условия из 
 (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
 5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов
"""

pass_wrong = ['Qwerty123', 'admin', 'password', '123456789', 'qwerty', '']
pass_detail = [False, False, False, False]
password = input('Введите пароль: ')
symbol_count = len(password) > 8
for symbol in password:
    if symbol.isdigit():
        pass_detail.pop(0)
        pass_detail.insert(0, True)
    elif symbol.islower():
        pass_detail.pop(1)
        pass_detail.insert(1, True)
    elif symbol.isupper():
        pass_detail.pop(2)
        pass_detail.insert(2, True)
    elif string.punctuation.find(symbol):
        pass_detail.pop(3)
        pass_detail.insert(3, True)
    else:
        ...
if pass_wrong.count(password) > 0:
    pass_complexity = 1
elif symbol_count and pass_detail.count(True) == 4:
    pass_complexity = 5
elif pass_detail.count(True) == 3:
    pass_complexity = 4
elif pass_detail.count(True) == 2:
    pass_complexity = 3
elif pass_detail.count(True) == 1:
    pass_complexity = 2
else:
    pass_complexity = 'Error'
print(f'\nНадежность вашего пароля: {pass_complexity}')
