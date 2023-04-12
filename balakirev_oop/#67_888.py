'''Обращаю внимание желающих, что функция map() возвращает итератор,
именно поэтому print(sum(map())) - работает;

a = map(float, ...) --> print(sum(a)) - работает,
а конструкция num1, num2 = map(float, ...) --> print(sum(num1, num2))
работать не будет(TypeError: 'float' object is not iterable), так как sum()
работает тоже с итератором(например, списком), поэтому чтобы print(sum(num1, num2))
заработал, надо из ДВУХ разных объектов -  чисел, сделать ОДИН итерируемый объект -
например список: print(sum([num1, num2]))

Итерируемый объект – это объект, который можно проитерировать, т.е. пройтись по элементам объекта в цикле.'''
# a, b = map(float, input().split())
# res = sum([a, b])
# print(res)

x, y = map(int, input().split())
black = x * 2
red = y * 4
print(sum([x, y, black, red]))
