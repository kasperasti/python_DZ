# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _damage(self, armor):
        return self.damage / armor

    def attack(self, person):
        print(f'Атакует {self.name}. Урон {self._damage(person.armor)}')
        person.health -= self._damage(person.armor)

    def get_heath(self):
        print(f'У {self.name} осталось {self.health} здоровья\n')

class Player(Person):
    pass

class Enemy(Person):
    pass

def get_heath(person):
    person.get_heath()

player = Player("Викинг", health=200, damage=100, armor=1.8)
enemy = Enemy("Гоблин", health=210, damage=110, armor=1.6)

while True:
    player.attack(enemy)
    get_heath(enemy)
    enemy.attack(player)
    get_heath(player)

    if enemy.health <= 0:
        print(f"Победил {player.name}")
        break
    if player.health <= 0:
        print(f"Победил {enemy.name}")
        break
