"""
Запросить у пользователя число N
Запросить у пользователя N целых чисел и записать их в список A
Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min и max). Вывести эти числа.
"""

number = ''
A = []
max_value = 0
min_value = 0
N = int(input('Enter N: '))
if N != 0:
    for i in range(N):
        while True:
            number = input(f'Enter number #{i+1}: ')
            if number.isdigit() or (number[0] == "-" and number[1:].isdigit()):
                A.append(int(number))
                break
            else:
                print('Wrong number')
    min_value = A[0]
    max_value = A[0]
    for j in A:
        if j > max_value:
            max_value = j
        if min_value > j:
            min_value = j
    print(f'\nmax:  {max_value}')
    print(f'min:  {min_value}')
else:
    print('\nError. Empty list')
