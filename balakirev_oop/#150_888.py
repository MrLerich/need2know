s = input()
a = s.replace(' ', '\'', 1)
b = a.replace(' ', '\"')
print(b)

# print('"'.join(input().split()).replace('"', "'", 1))