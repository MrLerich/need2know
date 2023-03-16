# Создание словаря из списков

street = ['a', 'b', 'c', 'd']
house_number = [1, 2, 3, 4]

def create_dct(lst1: list, lst2: list):
    for i in range(len(house_number)):
        new_dct = dict(zip(lst1, lst2))
    print(new_dct)

## Этот метод вызовет оошибку при разном количестве элементов в списках
# for i in range(len(house_number)):
#     c[street[i]] = house_number[i]
# print(c)

if __name__ == '__main__':
    create_dct(street, house_number)

