"""
Задание 5: Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом,
находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре со сдвигом
вправо на 3, А была бы заменена на Г, Б станет Д, и так далее. Нужно реализовать шифрование с помощью Python.
Пользователь вводит строку которую хочет зашифровать и число (сдвиг), нужно с помощью шифра Цезаря ее зашифровать и
вывести на экран. Выполнить задание нужно с помощью цикла for и строк, для получения числового представления символа
можно использовать ord, а для преобразования числа в строку - chr.
"""


message = input('Введите ваше сообщение на ru/ EN языке: ')
shift = int(input('Шифруем со сдвигом вправо: '))
encrypt_message = ''
for letter in message:
    if 1040 <= ord(letter) <= 1072 and letter.isupper():
        encrypt_message += chr(ord('А') + (ord(letter) - ord('А') + shift) % 32)
    elif 1072 <= ord(letter) <= 1103 and letter.islower():
        encrypt_message += chr(ord('а') + (ord(letter) - ord('а') + shift) % 32)
    elif 65 <= ord(letter) <= 90 and letter.isupper():
        encrypt_message += chr(ord('A') + (ord(letter) - ord('A') + shift) % 26)
    elif 97 <= ord(letter) <= 122 and letter.islower():
        encrypt_message += chr(ord('a') + (ord(letter) - ord('a') + shift) % 26)
print(f'\nЗашифрованное сообщение: {encrypt_message}')



