from collections import Counter
#Как узнать сколько ключей в словаре имеют одинаковые значения?
#Имеется dict состоящий из пар ключ: строка в юникоде,
# значение: целое число(int).
# Можно ли узнать (вывести) у скольких ключей значения совпадают?
dct = {
        u'DC963982-0B06-47D4-8E09-9D12C98FEEE4': 3,
        u'DC963983-0B06-47D4-8E09-9D12C98FEEE4': 3,
        u'D2AEE06F-B0BF-41E9-8646-93F7B852F357': 6
    }

values = dct.values()
counter = Counter(values)

print(dict(counter))