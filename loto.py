#!/usr/bin/pythok3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import re
import random


class Card:
    def __init__(self):
        self._card_template = str("+----+----+----+----+----+----+----+----+----+\n"
                                  "|j0k0|j0k1|j0k2|j0k3|j0k4|j0k5|j0k6|j0k7|j0k8|\n"
                                  "+----+----+----+----+----+----+----+----+----+\n"
                                  "|j1k0|j1k1|j1k2|j1k3|j1k4|j1k5|j1k6|j1k7|j1k8|\n"
                                  "+----+----+----+----+----+----+----+----+----+\n"
                                  "|j2k0|j2k1|j2k2|j2k3|j2k4|j2k5|j2k6|j2k7|j2k8|\n"
                                  "+----+----+----+----+----+----+----+----+----+\n")

        self.card = ""
        self.card_numbers = {}
        self._create_number()
        self._random_values()
        self._fill_card()

    def _generate_empty_field(self, lst_full_nums):
        return_lst_full_nums = lst_full_nums
        lst_emply_fild_off = []
        for n in range(0, 4):
            num = random.randint(0, 8)
            while num in lst_emply_fild_off:
                num = random.randint(0, 8)
            else:
                return_lst_full_nums[num] = ''
                lst_emply_fild_off.append(num)
        return return_lst_full_nums

    def _create_number(self):
        pattern = 'j[0-9]k[0-9]'
        keys = re.findall(pattern, self._card_template)
        i = 0
        for el in keys:
            self.card_numbers[el] = i
            i += 1

    def _random_values(self):
        lst_nums_all = []
        lst_num_off = []
        for s in range(0, 3):
            lst_nums = []
            for n in range(0, 9):
                num = random.randint(1, 90)
                while num in lst_num_off:
                    num = random.randint(1, 90)
                else:
                    lst_nums.append(num)
                    lst_num_off.append(num)
            lst_nums_all.append(self._generate_empty_field(sorted(lst_nums)))

        lst_nums_all = [j for i in lst_nums_all for j in i]

        for key, values in self.card_numbers.items():
            self.card_numbers[key] = lst_nums_all[values]

    def _fill_card(self):
        self.card = self._card_template
        for key, value in self.card_numbers.items():
            value_card = f' {str(value).rjust(2, "0")} '
            if not value:
                value_card = str().ljust(4, " ")
            self.card = re.sub(key, value_card, self.card)

    def card_empty(self):
        lst_check = len([value for value in self.card_numbers.values() if type(value) == type(int())])
        if lst_check == 0:
            return True
        else:
            return False

    def search_num(self, search_num):
        for key, values in self.card_numbers.items():
            if search_num == values:
                return True
        return False
    
    def del_num(self, del_num):
        for key, values in self.card_numbers.items():
            if del_num == values:
                self.card_numbers[key] = "**"
        self._fill_card()

    def print_card(self):
        print(self.card)


class Game():
    def __init__(self):
        self.player = None
        self.computer = None
        self.lst_bar_on_game = []
        self.lst_bar_off_game = []

    def gen_num(self):
        index_bar = random.randint(0, len(self.lst_bar_on_game) - 1)
        number_bar = self.lst_bar_on_game[index_bar]
        self.lst_bar_off_game.append(number_bar)
        del self.lst_bar_on_game[index_bar]
        return number_bar

    def end_game(self):
        if self.player.card_empty():
            print('ВЫ ПОБЕДИЛИ')
            return True
        elif self.computer.card_empty():
            print('ПОБЕДИЛ КОМПЬЮТЕР')
            return True
        else:
            return False

    def start_game(self):
        self.lst_bar_on_game = [n for n in range(1, 91)]
        self.player = Card()
        self.computer = Card()
        print("НАЧАЛО ИГРЫ\n")
        while True:
            if self.end_game():
                break
            print("Карточка игрока")
            self.player.print_card()
            print("")
            print("Карточка компьютера")
            self.computer.print_card()
            bar_num = self.gen_num()
            
            print(f"Новый бочонок: {bar_num} (осталось {str(len(self.lst_bar_on_game))})")
            self.computer.del_num(bar_num)

            answer = str(input("Зачеркнуть цифру? (y/n) "))
            if answer in ["y", "yes"]:
                if self.player.search_num(bar_num):
                    self.player.del_num(bar_num)
                else:
                    print(f"ВЫ ПРОИГРАЛИ! Боченка под номером: {bar_num} нет на карточке\n")
                    break
            else:
                if self.player.search_num(bar_num):
                    print(f"ВЫ ПРОИГРАЛИ! Боченка под номером: {bar_num} есть на карточке\n")
                    break

                                              
game = Game()
game.start_game()


