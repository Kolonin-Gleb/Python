# def sumInRange(start, end):
#     result = 0

#     while start <= end:
#         result += start
#         start += 1

#     return result

# # print(sumInRange(0, 10))


# def sumOfSquareOfNumsInRange(start, end):
#     result = 0

#     while start <= end:
#         result += start**2
#         start += 1

#     return result

# # print(sumOfSquareOfNumsInRange(0, 10))

# def sumOfCubesOfNumsInRange(start, end):
#     result = 0

#     while start <= end:
#         result += start**3
#         start += 1

#     return result

# print(sumOfCubesOfNumsInRange(0, 5))


# def sum_of(start, end, action): #Передача функции в функцию
#     result = 0
#     for i in range(start, end+1):
#         result+= action(i)
#     return result

# #Функции
# def ints(x): return x
# def squares(x): return x ** 2
# def cubes(x): return x ** 3

# print(sum_of(0, 5, ints))
# print(sum_of(0, 5, squares))
# print(sum_of(0, 5, cubes))


# Тут мы прошли labda функции, но я не успел


# ls = list(range(3, 10))

# index = 0

# for lsElem in ls:
#     ls[index] = str(ls[index])
#     index += 1

# print(ls)


# #                  Функциональное программирование


# ls = list(range(3, 10))
# print(ls)

# ls = list(map(str, ls)) #map - проходится по всем элементам последовательности # Приводим к типу list, т.к. вернет объект
# print(ls)


# filter()


# from functools import reduce

# # ls = [9, 6, 3, 5, 1]

# # res = reduce(lambda x, y: x + y, ls)
# # # reduce - складывает промежуточный результат со следущим элементом
# # print(res)


# ls = [9, 6, 3, 5, 1]
# res = reduce(lambda x, y: y if x < y else x, ls)
# print(res)

