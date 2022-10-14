"""
Пользователь вводит текст нужно вывести количество цифр в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество цифр: 3
"""

digit_list = []
digit_count = 0
text = input('\nВведите случайный текст:\n')
for i in range(len(text)):
    if text[i].isdigit():
        digit_list.append(int(text[i]))
digit_count = len(digit_list)
print(f'\nКоличество цифр: {digit_count}')
