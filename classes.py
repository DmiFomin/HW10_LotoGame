import random


class Card:

    def __init__(self, name, is_comp):
        self._name = name
        self._is_comp = is_comp
        self._remaining_numbers = 15
        self._is_in_game = True

        # Генерим 15 уникальных чисел
        randnum = random.sample(range(1, 91), 15)
        # Разбиваем по 5 и сортируем
        lines = [sorted(randnum[0:5]), sorted(randnum[5:10]), sorted(randnum[10:15])]
        card = []

        for line in lines:
            i = 0
            # Генерим расположение чисел в каждой строке
            place_numeric = sorted(random.sample(range(0, 9), 5))
            # Если место расположения для числа, то берем его, иначе 0
            for place in range(0, 9):
                if place in place_numeric:
                    num = line[i]
                    i += 1
                else:
                    num = 0
                card.append(num)

        self._card = card

    @property
    def name(self):
        return self._name

    @property
    def is_comp(self):
        return self._is_comp

    @is_comp.setter
    def is_comp(self, val):
        self._is_comp = val

    @property
    def remaining_numbers(self):
        return self._remaining_numbers

    @remaining_numbers.setter
    def remaining_numbers(self, val):
        self._remaining_numbers = val

    @property
    def is_in_game(self):
        return self._is_in_game

    @is_in_game.setter
    def is_in_game(self, val):
        self._is_in_game = val

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, val):
        if len(val) != 27:
            raise Exception('Карточка должна содержать 27 ячеек!')
        self._card = val

    def print_card(self):
        print('Карточка', 'компьютера' if self.is_comp else 'игрока', self.name)
        print(f'Осталось чисел: {self.remaining_numbers}')
        print('--------------------------')
        lines = [self.card[0:9], self.card[9:18], self.card[18:27]]
        for line in lines:
            line_str = ''
            for num in line:
                if num == -1:
                    line_str = f'{line_str} - '
                elif num == 0:
                    line_str = f'{line_str}   '
                elif num < 10:
                    line_str = f'{line_str} {num} '
                else:
                    line_str = f'{line_str}{num} '
            print(line_str.rstrip())

        print('--------------------------')

    def remove_number(self, number):
        if number in self.card:
            self.card = [-1 if num == number else num for num in self.card]
            self.remaining_numbers -= 1

    def check_answer(self, answer, num):
        if answer == 'y':
            if num in self.card:
                self.remove_number(num)
                result = True
            else:
                result = False
        if answer == 'n':
            if num in self.card:
                result = False
            else:
                result = True

        return result


class Bag:

    def __init__(self):
        self._set_numbers = random.sample(range(1, 91), 90)
        self._remaining_numbers = 90
        self._dropped_numbers = []

    @property
    def set_numbers(self):
        return self._set_numbers

    @set_numbers.setter
    def set_numbers(self, val):
        self._set_numbers = val

    @property
    def remaining_numbers(self):
        return self._remaining_numbers

    @remaining_numbers.setter
    def remaining_numbers(self, val):
        self._remaining_numbers = val

    @property
    def dropped_numbers(self):
        return self._dropped_numbers

    @dropped_numbers.setter
    def dropped_numbers(self, val):
        self._dropped_numbers = val

    def get_number(self):
        random.shuffle(self.set_numbers)
        number = random.choice(self.set_numbers)
        self.set_numbers.remove(number)
        self.remaining_numbers -= 1
        self.dropped_numbers.append(number)

        return number