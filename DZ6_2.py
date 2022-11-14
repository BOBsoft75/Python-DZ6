# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# первоначальое решение:

# import random
# num = int(input('Введите количество элементов списка: '))
# numList = []
# sum = 0
# for i in range(num):
#     numList.append(random.randrange(10))
# print(f'Список: {numList}')
# for i in range(1, len(numList), 2):
#     sum = sum + numList[i]
# print(f'{numList} -> сумма элементов на нечетных позициях: {sum}')


# решение с использованием filter:

from random import randint
num = int(input('Введите количество элементов списка: '))
numList = [randint(1, num) for i in range(num)]
print(f'Изначальный список: {numList}')
numList2 = [numList[i] for i in filter(lambda x: x % 2 == 1, range(num))]
print(
    f'Список элементов с нечетными индексами: {numList2} и их сумма: {sum(numList2)}')
