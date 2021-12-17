# import re
# from functools import reduce

# ls = 'люди прекрасно умеют хранить секреты, которых не знают.'.split()
# # Найти слово с максимальным количеством гласных букв

# vowels = r'[аеёиоуыэюя]'

# maxVowelWord = reduce(lambda x, y: x if len(re.findall(vowels, x)) > len(re.findall(vowels, y)) else y, ls)

# print(maxVowelWord)


# a = [1, 2, 3]
# # b = (True, False, True )
# c = {'1', '2', '3'}
# res = dict(zip(c, a))
# print(res)

#zip - объединяет элементы из разных последовательностей


# def mul5(x): return x * 5
# inc = lambda x: x + 1

# res = mul5(inc(10)) #Выполнение из нутри наружу

# print(res)


# Функция - композиция
# def compose(f, g):
#     return lambda x: f(g(x))

# def mul5(x): return x * 5
# inc = lambda x: x + 1

# inc_and_mul5 = compose(mul5, inc)
# mul5_and_inc = compose(inc, mul5)

# print(inc_and_mul5(10))
# print(mul5_and_inc(10))


# Замыкание

# def print_msg(msg):
#     def printer(rec):
#         print(f"To: {rec}. Msg: {msg}")
#     return printer

# print(print_msg("ahsdjkfh"))

def add(x):
    return lambda y: x + y

a = add(100)
print(a(5))

