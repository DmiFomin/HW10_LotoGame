import random

def generate_card():
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

    return card