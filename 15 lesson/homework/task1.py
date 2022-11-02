import pprint


"""
Необходимо создать класс Human с атрибутами:
name
surname
age
phone
address
Атрибуты должны заполняться в методе __init__

Так-же нужно написать методы:
get_info() - который возвращает словарь в котором находится информация о человеке
call(phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
Нужно создать 3 обьекта класса Human и вызвать у них метод get_info

В качестве решения нужно отправить ссылку на GitHub репозиторий.
"""


class Human:

    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return self.__dict__

    def call(self, phone_number):
        print(f'{self.phone} вызывает абонента {phone_number}')


Anton = Human('Anton', 'Honcharuk', 30, '+380937778899', 'City gb')
Max = Human('Max', 'Plaxoy', 25, '+380938978899', 'City sd')
Vasyl = Human('Vasyl', 'Petrov', 41, '+380937778300', 'City ds')
phone_number = 3700

pprint.pprint(Anton.get_info())
Anton.call(phone_number)
print('----------------------\n')
pprint.pprint(Max.get_info())
Anton.call(phone_number)
print('----------------------\n')
pprint.pprint(Vasyl.get_info())
Anton.call(phone_number)
print('----------------------')
