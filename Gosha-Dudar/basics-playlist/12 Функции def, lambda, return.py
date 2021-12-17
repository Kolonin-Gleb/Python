# def func (x):
#     def add (a):
#         return x + a
#     return add

# test = func(100) # Записываем функцию в переменную
# # x = 100
# print(test(200)) # Происходит запись значения а. Затем выполняется функция add

# def function():
#     pass # Ничего не возращать

# print(function())


# # Функции с неизвестным количеством параметров
# def func(*args):
#     print(args) # Выводит кортеж

# func(1, 2, 4, 24)

# def func(**args):
#     print(args) # Выводит словарь

# func(a = 24, b = 17, c = 7)


# lambda функции - короткие, одноразовые функции

add = lambda x, y: x*y # Запись lambda функции в переменную
print(add(2, 5))

# Выполнение lambda функции без исп. доп. пер.
print( (lambda x, y: x*y)(2, 6) )


