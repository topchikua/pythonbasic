task = '''Написать программу которая запрашивает у пользователя (с помощью функции input) 2 числа:
Сторона А и Высота h
Программа должна по формуле вычислить площадь треугольника и вывести ее пользователю.'''
A = float(input(task + '\nВведіть сторону трикутника: '))
h = float(input('А тепер висоту: '))

print('\nПлоща трикутника = ', + round(A / 2 * h, 2))
