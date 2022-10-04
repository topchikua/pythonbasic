"""
Запросить у пользователя 10 чисел и записать их в список A
Запросить у пользователя число N
Вывести пользователю сколько в списке A повторяется число N
"""

count = 10
num_list = []
for i in range(count):
    numbers = float(input(f'Enter number #{i + 1}: '))
    num_list.append(numbers)
N = float(input('\nEnter N: '))
print(f'In List: {num_list}\n{num_list.count(N)} coincidences')
