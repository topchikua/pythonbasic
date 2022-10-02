

# text = input("Enter text: ")
# shift = int(input("Enter shift: "))
#
# result = ''
#
#
# for symbol in text:
#     if symbol.islower():
#         result += chr(ord('а') + (ord(symbol) - ord('а') + shift) % 32)
#     elif symbol.isupper():
#         result += chr(ord('А') + (ord(symbol) - ord('А') + shift) % 32)
#
# print(result)

for i in range(ord('A'), ord('A') + 26):
    print(f'{i} = {chr(i)}')

# for i in range(ord('Ї'), ord('Ї') + 33):
#     print(f'{i} = {chr(i)}')
#
# for i in range(ord('Є'), ord('Є') + 33):
#     print(f'{i} = {chr(i)}')






