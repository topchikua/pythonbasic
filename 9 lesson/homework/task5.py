"""
Запросить у пользователя 5 чисел и записать их в список A
Записать все числа из списка A которые больше 5 в список C
"""

count = 5
A = []
C = []
for i in range(count):
    number = float(input(f'Enter Number #{i+1}: '))
    A.append(number)
for j in range(len(A)):
    if A[j] > 5:
        C.append(A[j])
print(f'\nA: {A}\nC: {C}')
