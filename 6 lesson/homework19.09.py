star = '*'

'''1. Вывести треугольник #1 с шириной N с помощью цикла while
*****
****
***
**
*'''

N = int(input('Введіть ширину трикутника: '))

while N > 0:
    print(star * N)
    N -= 1


'''2. Вывести треугольник #2 с шириной N с помощью цикла while
*
**
***
****
*****'''

N = int(input('Введіть ширину трикутника: '))
i = 0

while N > i:
    i += 1
    print(star * i)


'''3. Вывести треугольник #3 с шириной N с помощью цикла while
*****
 ****
  ***
   **
    *'''

N = int(input('Введіть ширину трикутника: '))
i = 0

while N > 0:
    print(i * ' ' + star * N)
    i += 1
    N -= 1


'''4. Вывести треугольник #4 с шириной N с помощью цикла while
    *
   **
  ***
 ****
*****'''

N = int(input('Введіть ширину трикутника: '))
i = 0
j = N

while N > i:
    j -= 1
    i += 1
    print(' ' * j + star * i)
    