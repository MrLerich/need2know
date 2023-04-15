# # 1
# def chain_sum(number):
#     result = number
#     def wrapper(number2=None):
#         nonlocal result
#         if number2 is None:
#             return result
#         result += number2
#         return wrapper
#     return wrapper


# # 2
# def chain_sum(number):
#     result = number
#     def wrapper(number2=None):
#         nonlocal result
#         try:
#             number2 = int(number2)
#         except TypeError:
#             return result
#         result += number2
#         return wrapper
#     return wrapper
#
#
# # 3
# def chain_sum(number):
#     def wrapper(number2=None):
#         if number2 is None:
#             return wrapper.result
#         wrapper.result += number2
#         return wrapper
#     wrapper.result = number
#     return wrapper
#
#
# # 4
# def chain_sum(number):
#     def wrapper(number2=None):
#         def inner():
#             wrapper.result += number2
#             return wrapper
#         logic = {
#             type(None): lambda: wrapper.result,
#             int: inner
#         }
#         return logic[type(number2)]()
#     wrapper.result = number
#     return wrapper
#
#
# # 5
# class chain_sum:
#     def __init__(self, number):
#         self._number = number
#
#     def __call__(self, value=0):
#         return chain_sum(self._number + value)
#
#     def __str__(self):
#         return str(self._number)
#
#
# 6
class chain_sum(int):
    def __call__(self, addition=0):
        return chain_sum(self + addition)



print(chain_sum(5)())   # 5
print(chain_sum(5)(7)())    # 12
print(chain_sum(5)(100)(-10)())     # 95


