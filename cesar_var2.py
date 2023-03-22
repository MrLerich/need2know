# ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits = '0123456789'
# hexdigits = '0123456789abcdefABCDEF'
# octdigits = '01234567'
# printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
# punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# whitespace = ' \t\n\r\x0b\x0c'


ascii_lowercase: str = 'abcdefghijklmnopqrstuvwxyz'
shift: int = 3      # сдвиг
alpha_shift: str = ascii_lowercase[shift:]      # что срезаю и прибавляю в конец алфавита
alphabet: str = alpha_shift + ascii_lowercase[:shift]        # новый алфавит
code_dct: dict = dict(zip(ascii_lowercase, alphabet))     # словарь старая буква:новая буква
txt: str = input('Input text: ')     # что кодируем
# txt_lst: list = txt.split()
# inttxt = ''.join(txt_lst)
# key_dct = code_dct.keys()
# val_dct = code_dct.values()
outtxt = []
for i in txt:
    if i in code_dct.keys():
        outtxt.append(code_dct[i])
    else:
        outtxt.append(i)
print(''.join(outtxt))
