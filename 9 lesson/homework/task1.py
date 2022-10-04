"""
Запросить у пользователя 5 чисел и записать их в список
"""

count = 5
num_list = []
for i in range(count):
    numbers = float(input(f'Enter number #{i + 1}: '))
    num_list.append(numbers)
print(f'\nNew List\n{num_list}')
