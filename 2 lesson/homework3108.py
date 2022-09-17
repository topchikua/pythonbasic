task1 = '''\n\n\nЗадание максимум на 90 баллов:
- Вывести на экран строку "Hello world"
- Вывести на экран пять звездочек (*)'''
task2 = '''Задание со звездочкой:
Вывести на экран квадрат 5 на 5 заполненный символами'''

print(task1)
msg1 = '\nРішення:\n1. Доброго вечора, ми з України'
star = '*'
print(msg1)
print("2. 5 зірок: ", star * 5, '\n')

print(task2)
symbol = input('\nВкажіть символ для заповнення:\n')
count = 5

'''print(5 * (symbol + ' '))
print((symbol + ' ') * 5)
print((symbol + ' ') * 5)
print((symbol + ' ') * 5)
print(5 * (symbol + ' '))
##### Пример некачественного кода 
'''


print(((symbol + ' ') * count + '\n') * count)
