import json

"""
Дано два словаря
A = {'key': 1}
B = {'key1: 2}
Необходимо написать код который будет их объединять
C = {'key': 1, 'key1': 2}
Но нужно так-же учитывать коллизии, например ситуация когда у нас два одинаковых ключа и чтобы не потерять значения 
нужно записать в один ключ список в котором будут находится значения
Например:
A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}
C = {'key': [1, 'Hello'], 'key2': True}
Записать результат в файл result.json в формате JSON.
"""

A = {'name': 'Anton', 'phone': '+380997775544', 'id': 7771}
B = {'name': 'Max', 'id': 7772, 'email': 'test@gmail.com'}
C = {**A, **B}

for key, value in B.items():
    if A.get(key):
        C[key] = [A[key], value]
    else:
        C[key] = value
result = json.dumps(C)

with open('result.json', 'w') as f:
    f.write(result)
print(f'Запись успешно сохранена\nJSON: {result}')