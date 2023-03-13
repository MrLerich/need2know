#  Single Responsibility principle

#  Принцип единственной обязанности

# class User:
#     def __init__(self, name: str):
#         self.name = name
#
#     def get_name(self) -> str:
#         pass
#
#     def save(self, user: User):
#         pass


class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass

class UserDB:
    def get_user(self, id: int) -> User:
        pass
    def save(self, user: User):
        pass