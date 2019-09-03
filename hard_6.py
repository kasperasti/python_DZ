# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Manufacture:
    def __init__(self,type_toy):
        self.type_toy = type_toy

    def buying(self):
        print('Закупаем сырье')
    def sewing(self):
        print('Вышиваем игрушку')
    def painting(self):
        print('Окрашиваем игрушку')
def choise_user():
    if choise == 1:
        Toy = WinnieThePooh
    elif choise == 2:
        Toy = ToyCar
    elif choise == 3:
        Toy = Doll

choise = (input('Выберите тип игрушки: \n'
                         '1. Мягкая игрушка \n'
                         '2. Машинка \n'
                         '3. Кукла \n'))

class Toy:
    def __init__(self, name, color, type_toy):
        self.name = name
        self.color = color
        self.type_toy = type_toy

class WinnieThePooh(Toy):
    def music(self):
        print('Напевает песню: Кто ходит в гости по утрам')

winniepooh = WinnieThePooh ('Винни Пух', 'коричневый', 'мягкая игрушка')


class ToyCar(Toy):
    def drag(self):
        print('Машинка начала резкое ускорение')

class Doll(Toy):
    def love(self):
        print('Кукла говорит, что любит вас')