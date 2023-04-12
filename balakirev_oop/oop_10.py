# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/butyKEUntK0
#
# Подвиг 10. Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:
#
# add(self, eng, rus) - для добавления новой связки английского и русского слова (если английское слово уже существует, то новое русское слово добавляется как синоним для перевода, например, go - идти, ходить, ехать); если связка eng-rus уже существует, то второй раз ее добавлять не нужно, например:  add('go', 'идти'), add('go', 'идти');
# remove(self, eng) - для удаления связки по указанному английскому слову;
# translate(self, eng) - для перевода с английского на русский (метод должен возвращать список из русских слов, соответствующих переводу английского слова, даже если в списке всего одно слово).
#
# Все добавления и удаления связок должны выполняться внутри каждого конкретного объекта класса Translator, т.е. связки хранить локально внутри экземпляров классов класса Translator, используя коллекцию-словарь. (Хранить связки в коллекции __dict__ не нужно! Определите для этого отдельный словарь.)
#
# Создайте экземпляр tr класса Translator и вызовите метод add для следующих связок:
#
# tree - дерево
# car - машина
# car - автомобиль
# leaf - лист
# river - река
# go - идти
# go - ехать
# go - ходить
# milk - молоко
#
# Затем методом remove() удалите связку для английского слова car. С помощью метода translate() переведите слово go. Результат выведите на экран в виде строки из всех русских слов, связанных со словом go:
#
# Вывод в формате: идти ехать ходить
# class Translator:
#     def add(self, eng, rus):
#         if eng not in self.__dict__:
#             setattr(self, eng, [rus])
#         else:
#             self.__dict__[eng].append(rus)
#
#     def remove(self, eng):
#         self.__dict__.pop(eng, None)
#
#     def translate(self, eng):
#         return self.__dict__[eng]

class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}
        self.tr.setdefault(eng, [])

        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        self.tr.pop(eng, False)

    def translate(self, eng):
        return self.tr[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove('car')
print(*tr.translate('go'))

#
# for pair_of_words in ('tree - дерево', 'car - машина', 'car - автомобиль',
#                       'leaf - лист', 'river - река', 'go - идти',
#                       'go - ехать', 'go - ходить', 'milk - молоко'):
#     tr.add(*pair_of_words.split(' - '))
