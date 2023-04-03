s: str = 'hieeelalaooo'     #  hieeelalaooo
lst_s: list = list(s)
print(lst_s)
vowels: str = 'aeiouy'
v_lst: list = list(vowels)
# print(v_lst)
for i in lst_s:
    if i in v_lst:
        lst_s.remove(i)

print(lst_s)

# while i < len(s):
#     print(s[i], end='')
#     i += [2, 3][s[i] in 'aeiouy']

# s_1 = re.sub(r'([aeiouy])\1\1', r'\1', test_str)
# s_2 = re.sub(r'(([^aeiouy])[aeiouy])', r'\2', s_1)


# # List of integers
# lis = [1, 4, 2, 6, 1, 9, 10]
#
# # Value to be removed
# val = 6
#
# # Check if the list contains the value
# if val in lis:
#
# 	# Remove the value from the list
# 	lis.remove(val)
#
# # Printing the list
# print(lis)

# lst = [0, 95, 0, 76, 0, 23, 68, 0, 23, 156, 95]
# seq = iter(lst)
# newlst=[]
# try:
#     for _ in seq:
#         newlst.append(_)
#         if _==0:
#             next(seq)
# except StopIteration:
#     pass
# print(newlst)