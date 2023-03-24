class Singleton:
    """Шаблон предоставления глобального доступа к состоянию, объект всегда один """
    instance = None  # изначально нет

    def __new__(cls):
        if Singleton.instance is None:  # проверяем есть что, нет - создаем инстанс от родителя object
            Singleton.instance = super().__new__(cls)
        return Singleton.instance


if __name__ == '__main__':
    first = Singleton()
    second = Singleton()
    print(first, second, first is second, sep='\n')


# class Singleton(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance
#
#
# # В этом фрагменте кода мы переопределяем метод __new__ (специальный метод Python для создания объектов),
# # что бы управлять созданием объекта. Объект s создается с помощью метода __new__, но перед этим он проверяет,
# # существует ли уже созданный объект. Метод hasattr (специальный метод Python, позволяющий определить, имеет ли объект
# # определенное свойство), используется для проверки наличия у объекта cls свойства instance. При создание объекта s,
# # объект просто создается. В случае создания объекта s1, hasattr() обнаруживает, что у объекта уже существует свойство
# # instance, и, следовательно, s1 использует уже существующий экземпляр объекта (расположенный по адресу 0x10ba9db90).
#
# if __name__ == '__main__':
#     s = Singleton()
#     print("Object created", s)
#     s1 = Singleton()
#     print("Object created", s1)

class Singleton:
    """
    Шаблон предоставления глобального доступа к состоянию, объект всегда один
    нужен для одной точки доступа к ресурсам/данным и для того
    чтобы ресурсоёмкие задачи сделать 1 раз
    плюсы: 1 раз выполняем тяжелые задачи имеет 1 вход для все системы
    минус: общесистемная глобальная переменная!!!
     """
    instance = None  # изначально нет

    def __new__(cls):
        if Singleton.instance is None:  # проверяем есть что, нет - создаем инстанс от родителя object
            Singleton.instance = super().__new__(cls)
            Singleton._do_work(Singleton.instance)
        return Singleton.instance

    def _do_work(self):
        print('do smth hard work')
        # parse, db, work with data/resources etc...
        self.data = 101

class Monostate:
    """
    Алекс Мортели
    Шаблон предоставления глобального доступа к состоянию, объекты могут быть разными
    В описание шаблона Singleton в книге Gang of Four говорится, что должен быть
    один и только один объект класса. Однако, согласно Алексу Мартелли,
    программисту обычно требуется, чтобы экземпляры имели одно и то же состояние.
    Он предлагает разработчикам больше беспокоиться о состоянии и поведении,
    а не об идентичности экземпляров. Поскольку концепция основана на том что бы все
     объекты имели одно и то же состояние, она также известна как шаблон Monostate.
     https://www.youtube.com/watch?v=4ZXGELFwfPA
     https://webdevblog.ru/realizaciya-shablona-singleton-v-python/
    """
    _shared__state = {}

    def __init__(self):
        self.__dict__ = self._shared__state
        if not self._shared__state:
            print('do smth hard work')
            # parse, db, work with data/resources etc...
            self.data = 101


if __name__ == '__main__':
    first = Singleton()
    print(first)
    second = Singleton()
    print(second)
    print(first is second)
    print(first.data)
    first.data = 102
    print(second.data)