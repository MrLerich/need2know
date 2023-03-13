#  Open/Closed principle

#  Принцип открытости/закрытости

# class Discount:
#     def __init__(self, customer, price: float):
#         self.customer = customer
#         self.price = price
#     def give_discount(self):
#         if self.customer == 'fav':
#             return self.price * 0.2
#         if self.customer == 'vip':
#             return self.price * 0.4

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price
    def get_discount(self):
        """просто скидка клиентам"""
        return self.price * 0.2

class VIPDiscount(Discount):
    def get_discount(self):
        """скидка випам - двойная"""
        return super().get_discount() * 2

class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        """это уже скидка супервипам -вдвое больше чем випам"""
        return super().get_discount() * 2

    # расширяем, но не модифицируем

