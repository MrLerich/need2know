# # Создание словаря из списков
#
# street = ['a', 'b', 'c', 'd', 'a']
# house_number = [1, 2, 3, 4, 5]
#
# def create_dct(lst1: list, lst2: list):
#     for i in range(len(house_number)):
#         new_dct = dict(zip(lst1, lst2))
#     print(new_dct)
#
# ## Этот метод вызовет ошибку при разном количестве элементов в списках
# # for i in range(len(house_number)):
# #     c[street[i]] = house_number[i]
# # print(c)
#
# if __name__ == '__main__':
#     create_dct(street, house_number)
#
#
#
from collections import defaultdict

street: list = ['a', 'b', 'c', 'd', 'a']
house_number: list = [1, 2, 3, 4, 5]

data_after_1st_step: list = list(zip(street, house_number))
print(f'data_after_1st_step: {data_after_1st_step}')


## ver1
# only_with_unique_street: dict = defaultdict(list)
# for i, j in data_after_1st_step:
#     only_with_unique_street[i].append(j)
#

# # https://www.geeksforgeeks.org/python-convert-list-of-tuples-to-dictionary-value-lists/
# print(f'only_with_unique_street: {str(dict(only_with_unique_street))}')

# Ver2 - мне он больше нра
only_with_unique_street = {}
for k, v in data_after_1st_step:
    only_with_unique_street.setdefault(k, []).append(v)
# # дальше времени не хватает - опять за руль :(
print(str(only_with_unique_street))