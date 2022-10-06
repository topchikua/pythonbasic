"""
Запросить у пользователя число N
Запросить у пользователя N чисел и записать их в список A
Вывести список в обратной последовательности
"""

N = int(input('Enter N: '))
numbers_list = []
for i in range(N):
    number = float(input(f'Enter number #{i+1}: '))
    numbers_list.append(number)
numbers_list.reverse()
print(f'\nResult: {numbers_list}')
