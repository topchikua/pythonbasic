task1 = ''' 1. Пользователь с клавиатуры вводит трех значное число в переменную number.
Переставьте первую и последнюю цифру переменной number, полученный результат запишите в переменную reversed_number. 
Важно, что переменная number обязательно должна быть типа данных int и для решения задачи можно использовать 
преобразование типов данных только при получении числа из функции input.'''

number = int(input(f'{task1}\nВведіть тризначне число: '))

if number < 0:
    number = number * -1
hundreds = number % 10 * 100
tenths = number // 10 % 10 * 10
digit = number // 100 % 10
reversed_number = hundreds + tenths + digit
print(f'\nНове число: {reversed_number}')


task2 = '''2. Пользователь вводит с клавиатуры три числа в переменные a, b, c.
Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no'''

a = int(input(f'\n{task2}\nВведіть А: '))
b = int(input('Введіть B: '))
c = int(input('Введіть C: '))
condition1 = bool(a > 10 and b > 10 and c > 10)
condition2 = bool(a % 3 == 0 and b % 3 == 0)

if condition1 is True and condition2 is True:
    print('\nYes')
else:
    print('\nNo')


task3 = '''3. Пользователь вводит с клавиатуры три числа в переменные a, b, c. 
Найдите наибольшее число из них и запишите в переменную max.'''

a = float(input(f'\n{task3}\nВведіть А: '))
b = float(input('Введіть B: '))
c = float(input('Введіть C: '))

if a >= b and a >= c:
    MAX = a
elif b >= c:
    MAX = b
else:
    MAX = c
print(f'\nНайбільше число: {MAX}')
