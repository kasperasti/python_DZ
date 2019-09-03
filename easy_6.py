# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


# class TownCar:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = False
#
#     def go(self):
#         print(f'Машина {self.name} going')
#     def stop(self):
#         print(f'Машина {self.name} stoping')
#     def turn(self):
#         direction = input('Куда повернуть машине? ')
#         print(f'Машина {self.name} повернула ' + direction)
#
# towncar = TownCar (160, 'black', 'ford', False)
#
# class SportCar:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = False
#
#     def go(self):
#         print(f'Машина {self.name} going')
#     def stop(self):
#         print(f'Машина {self.name} stoping')
#     def turn(self):
#         direction = input('Куда повернуть машине? ')
#         print(f'Машина {self.name} повернула ' + direction)
#     def nitro(self):
#         print(f'Машина {self.name} активировала нитро')
#
# sportcar = SportCar (250, 'red', 'toyota', False)
#
# class WorkCar:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = False
#
#     def go(self):
#         print(f'Машина {self.name} going')
#     def stop(self):
#         print(f'Машина {self.name} stoping')
#     def turn(self):
#         direction = input('Куда повернуть машине? ')
#         print(f'Машина {self.name} повернула ' + direction)
#     def load(self):
#         print('Машина загружается')
#
# workcar = WorkCar (140, 'blue', 'mitsubishi', False)
#
#
# class PoliceCar:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = True
#
#     def go(self):
#         print(f'Машина {self.name} going')
#     def stop(self):
#         print(f'Машина {self.name} stoping')
#     def turn(self):
#         direction = input('Куда повернуть машине? ')
#         print(f'Машина {self.name} повернула ' + direction)
#
# policecar = PoliceCar (180, 'white', 'lada', True)


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class TownCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Машина {self.name} going')

    def stop(self):
        print(f'Машина {self.name} stoping')

    def turn(self):
        direction = input('Куда повернуть машине? ')
        print(f'Машина {self.name} повернула ' + direction)

    def signal(self):
        print(f'Машина {self.name} посигналила')


car = TownCar(100, 'grey', 'Zaz', False)



class SportCar(TownCar):
    def nitro(self):
        print(f'Машина {self.name} активировала нитро')

sportcar = SportCar (250, 'red', 'Toyota', False)

class WorkCar(TownCar):
    def load(self):
        print('Машина загружается')

workcar = WorkCar (140, 'blue', 'Mitsubishi', False)

class PoliceCar(TownCar):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police = True)
        self.is_police = True

    def siren(self):
        print(f'Полицейская машина {self.name} включила сирену')

policecar = PoliceCar (180, 'white', 'Lada')
print(policecar.is_police)