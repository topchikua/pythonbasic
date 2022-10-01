ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

symbols = random.choices(ascii_lowercase, k=5)  # Сгенерировали 5 рандомных символов из букв ascii_lowercase
done_str = ''.join(symbols)
print(done_str)