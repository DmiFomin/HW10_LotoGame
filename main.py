from classes import Card, Bag


print('Начинаем нашу игру!')
count_players = ''
while not count_players.isdigit():
    count_players = input('Введите количество игроков: ')
    if not count_players.isdigit():
        print('Вам нужно ввести целое число!')

try:
    count_players = int(count_players)
except Exception as e:
    print(e)
    print('Ошибка! Попробуйте заново.')

cards = []
for i in range(0, count_players):
    answer = ''
    while (answer != 'y') and (answer != 'n'):
        answer = input(f'За игрока №{i + 1} играет компьютер (y/n)? ')
        if (answer != 'y') and (answer != 'n'):
            print('Некорректный ответ! Вам нужно ответить y - да или n - нет.')

    name_player = input(f'Введите имя игрока №{i + 1}: ') if answer == 'n' else f'Игрок {i+1}'
    cards.append(Card(name_player, False if answer == 'n' else True))


# cards.append(Card('Dima', False))
# cards.append(Card('Comp 1', True))
print('Карточки игроков: ')
for card in cards:
    card.print_card()

bag = Bag()
for i in range(0, len(bag.set_numbers)):
    current_number = bag.get_number()
    print(f'ХОД №{i + 1}')
    print(f'Выпавшие бочонки: {bag.dropped_numbers}')
    print(f'Новый бочонок: {current_number} (осталось {bag.remaining_numbers})')
    for card in cards:
        if not card.is_in_game:
            continue

        card.print_card()
        if card.is_comp:
            card.remove_number(current_number)
        else:
            answer = ''
            while (answer != 'y') and (answer != 'n'):
                answer = input(f'{card.name}, зачеркнуть цифру (y/n)? ')
                if (answer != 'y') and (answer != 'n'):
                    print('Некорректный ответ! Вам нужно ответить y - да или n - нет.')

            if not card.check_answer(answer, current_number):
                card.is_in_game = False
                print(f'{card.name}, Вы проиграли!')

    # Ищем победителя
    is_win = False
    for card in cards:
        if card.remaining_numbers == 0:
            print(f'ПОБЕДИТЕЛЬ - {card.name.upper()}')
            is_win = True

    if is_win:
        break

    print('Конец игры')