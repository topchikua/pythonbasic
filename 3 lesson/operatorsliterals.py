# # dddsd
# # defdd
# # d
# # d
# # d
# # d      command slash
#
# txt = 'fff'
# print(2 + 2)
# print(4 - 2)
# print(4 * 2)
# print(4 / 2)
# print('aaaa ' + txt)
# print(txt * 4)
# print(3 ** 3)
# print(5 / 2)
# print(10 // 3)
# print(10 % 3)
#
# print(10 < 5)
# print(10 > 5)
# print(10 <= 5)
# print(10 >= 5)
# print(10 == 10)
# print(10 != 11)

# a = 5
# print(a ** 5)
# a **= 5
# print(a)

# a = 'Hello Аnton'
# print('An' in a)
# print( ord('a'))
# print( ord('A'))
# print( ord('а'))
# print('\a')

name = 'Anton'
welcome_text = 'aaaaaa aaaaa aaaaa'
template = 'Hello {}!\n{}'
new_template = 'Hello %s!\n%s'
# print('hello ' + name + '!\n' + welcome_text)
print(new_template.format(name, welcome_text))
# print(template % (name, welcome_text))

print(f'Hello {name}!\n{welcome_text}')