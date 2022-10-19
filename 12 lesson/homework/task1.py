import pickle

"""
Дан список словарей, необходимо записать их в файл с помощью модуля pickle.
В каждом из словарей одинаковый набор ключей, а все значения представлены в виде строк
"""

users = [
    {
        'name': 'Honcharuk Anton',
        'email': 'test1@gmail.com',
    },
    {
        'name': 'Petrov Max',
        'email': 'test2@gmail.com'
    }
]
with open('users.txt', 'wb') as f:
    pickle.dump(users, f)
    f.write(pickle.dumps(users))
print(f'Данные успешно записаны\nCериализованный объект: \n{pickle.dumps(users)}')
