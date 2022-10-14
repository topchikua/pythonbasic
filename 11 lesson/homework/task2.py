"""
Права доступа
Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:
запись – W;
чтение – R;
запуск – X.
На вход программе подается:
число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.
"""

access_rights = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
}
permissions = {}
result = []

n = int(input('Введите количество файлов: '))
for i in range(n):
    key, *value = input(f'Файл {i+1}: ').split()
    permissions[key] = set(value)
m = int(input('Количество запросов: '))
for j in range(m):
    event, file = input(f'Запрос №{j+1}:\n').split()
    if access_rights[event] in permissions[file]:
        result.append('OK')
    else:
        result.append('Access denied')
print(*result, sep='\n')
