"""
Пользователь вводит текст нужно вывести количество цифр в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество цифр: 3
"""

digit_count = 0
digit_list = []
text = input('\nEnter the random text:\n')
for i in range(len(text)):
    if text[i].isdigit():
        digit_list.append(int(text[i]))
print(digit_list)
for j



