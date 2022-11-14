# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# первоначальное решение

# num = int(input('Введите число N: '))
# numList = list()
# result = 1
# for i in range(1, num+1):
#     result *= i
#     numList.append(result)
# print('N =', num, numList, end=' ')


# решение с map/lambda:
num = int(input('Введите число N: '))


def fact(x):
    f = 1
    for i in x:
        f *= i
    return f


numList = list(map(lambda x: fact(range(1, x + 1)), range(1, num + 1)))
print(numList)
