# Создайте программу для игры с конфетами человек против человека.

import random

sweets = 2021
print(f'Условия игры. На столе {sweets} конфета. Вы можете взять не более 28 конфет за один ход. Выигрывает тот, кто сделает последний ход.')
print()
count = random.randint(1, 2)

while sweets > 0:
    count = count + 1
    if count % 2 == 0:
        print('Ходит соперник')
        quantity = random.randint(1,28)
        print(quantity)
        print(f'Соперник забирает {quantity} конфет')
    else:
        quantity = int(input('Ваш ход: '))
    if 0 < quantity < 29:
        sweets = sweets - quantity
        print(f'Конфет осталось - {sweets}')
    else:
        print('Вы ввели некоректное кол-во конфет, введите число от 1 до 28')
        count = count - 1

if count % 2 == 0:
    print('Вы проиграли')
else:
    print('Поздравляем, победа Ваша!')