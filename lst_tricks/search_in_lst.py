# # Есть список вида [[10, 3], [20, 1], [11, 4], ...]
# # Можно ли так сформулировать поиск, чтобы искать входит
# # ли искомое число (например 12) во внутренние списки на первой позиции.
# # То есть нет ли числа 12 среди ряда 10, 20, 11 ...
# # и в случае, если входит, то получить индекс вида list[][]?
#
# ## 1
# # l = [[12, 3], [20, 12], [12, 4], [3, 4]]
# # # Находим индекс листа, содержащего 12 и индекс в этом листе:
# # n, x.index(12) for n, x in enumerate(l) if 12 in x
# #
# # # Находим индексы листов, в которых первый элемент 12:
# # n for n, x in enumerate(l) if x[:1] == [12]
# #
# # print(n, x)
#
#
# ## 2
# # collection_of_numbers = [[12, 3], [20, 1], [12, 4]]
# #
# # for index, list_of_numbers in enumerate(collection_of_numbers):
# #     if 12 == list_of_numbers[0]:
# #         print('list[{0:d}][0]'.format(index))
# #
# # indecec = [index for (index, list_of_numbers) in enumerate(collection_of_numbers) if list_of_numbers[0] == 12]
# # for index in indecec:
# #     print('list[{0:d}][0]'.format(index))
#
# ## 3
#
# # Чтобы узнать, есть ли 12 на первой позиции во вложенных списках:
# pairs = [[10, 3], [20, 1], [11, 4], [12, 4]]
# print(any(x == 12 for x, *_ in pairs))
# # Чтобы найти индекс пары cо значением 12 на первой позиции:
# print(next(i for i, (x, _) in enumerate(pairs) if x == 12))
# # Чтобы найти все индексы пар из списка, у которых на первой позиции 12:
# print([i for i, (x, _) in enumerate(pairs) if x == 12])
#
#
# ## 4
# # определяем как первый индекс так и все остальные (если надо)
#
# lst = [[12, 3], [20, 12], [12, 4], [3, 4], [124, 6], [12, 43]]  # имеем список списков
# res = []
# for i in lst:
#     res += i  # объединяем списки в один список
# # res=[12, 3, 20, 12, 12, 4, 3, 4, 124, 6, 12, 43]
#
# for n, x in enumerate(res[::2]):  # используем список res от 0 с шагом 2
#     if x == 12:
#         print(f'index - {n}, what we searching {x}')