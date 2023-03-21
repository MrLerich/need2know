# 1

import re

x = 'k3e10g88f13'

chars = re.findall(r'[a-zA-Z]+', x)  # ['k', 'e', 'g', 'f']
nums = re.findall(r'\d+', x)  # ['3', '10', '88', '13']

print(chars, nums, sep="\n")


# 2
x = 'k3e10g88f13'
word = []
number = []
for i in x:
    if i.isalpha():
        if not word or not last_isalpha:
            word.append(i)
        else:
            word[-1] += i
    else:
        if not number or last_isalpha:
            number.append(i)
        else:
            number[-1] += i
    last_isalpha = i.isalpha()
print(word, number, sep="\n")


# 3
x = 'k3e10g88f13'
word = "".join(" " if el.isdigit() else el for el in x).split()
number = "".join(el if el.isdigit() else " " for el in x).split()

print(word)
print(number)
