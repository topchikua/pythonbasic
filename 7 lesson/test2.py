import string

text = input("Enter text: ")
shift = int(input("Enter shift: "))

alphabet = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

result = ""
for i in text:
    if i in alphabet:
        result += alphabet[(alphabet.index(i) + shift) % 26]
    elif i in alphabet_upper:
        result += alphabet_upper[(alphabet_upper.index(i) + shift) % 26]
    else:
        result += i

print(result)