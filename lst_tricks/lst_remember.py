# lst = [1, (2, 3, 4), {2: 'b', 'c': [7, 8, 9]}, 'a', 'w', 't', 'f', 'e', 2, 3, 4, 5, 'r']
# lst_2 = lst * 3
# lst_3 = lst[1][2]
# lst_4 = lst[2] # а как из этого еще вытащить пары ключ - значение,
# # просто ключи(значения),
# # просто значения,
# # посчитать сумму значений ключа 'c' и подставить ее в значение ключа
# print(lst_2)
# print(lst_3)
# print(lst_4)

# 1 как определить тип данных хранящихся в списке
lst = [1, (2, 3, 4), {2: 'b', 'c': [7, 8, 9]}, 'a', 'w', 't', 'f', 'e', 2, 3, {6: 'b', 'c': [99, 45, 10]}, 4, 5, 'r']

# x = {2: 'b', 'c': [7, 8, 9]}

def decor_search(func):
    def wrapper(*args, **kwargs):
        pass

def sum_insert(d: dict):
    pass


def search_dict(lst: list):
    for i in lst:
        if type(i) is dict:  # опреляем что есть словари
            for k, v in i.items():
                if type(v) is list:  # в списке - узнать что есть инты
                    i[k] = sum(v)
                    print(k, i[k])
                else:
                    print(k, v)

search_dict(lst)
print(lst)



