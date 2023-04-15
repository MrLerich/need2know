a, b, c = input().split()
a = a.ljust(3, fillchar='0')
b = b.ljust(3, fillchar='0')
c = c.ljust(3, fillchar='0')

print(a, b, c)


# print('\n'.join([i.rjust(3,'0') for i in input().split()]))