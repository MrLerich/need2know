'''Подвиг 4. Допишите программу, в которой вводятся два слова (в переменные s1 и s2) в одну строчку через пробел, и отображаются в консоли в формате:

Word 1: s1 | Word 2: s2

Sample Input:

I love
Sample Output:

Word 1: I | Word 2: love'''
# ввод данных

# 1
print(' | '.join([f'Word {ind}: {el}' for ind, el in enumerate(map(str.strip, input().split()), 1)]))

# 2
s1, s2 = map(str.strip, input().split())

print("Word 1: %s | Word 2: %s" % (s1, s2))