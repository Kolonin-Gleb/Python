# print( (lambda x, y: x * y / 10)(5, 10))

# from random import randint
# ls = [randint(0, 50) for i in range(10)]

# print("Список до изменения: ")
# print(ls)

# check = lambda lsElem: lsElem -10 if lsElem > 5 else lsElem

# print("Список после изменения: ")
# ls = list(map(check, ls))
# print(ls)


# quote = 'Мудрец станет хозяином своего разума, глупец станет его рабом'
# ls = quote.split() # Получил список строк(слов)
# print(ls)
# # Найти индекс вхождения 1ой буквы а в каждом слове. Если не найден, то -1
# # S.find(str, [start],[end])	Поиск подстроки в строке. Возвращает номер первого вхождения или -1
# LsOfindexesOfAInWords = list(map(lambda word: word.find('а', 0, -1), ls))

# print(LsOfindexesOfAInWords)


ls = 'объединяет в кортежи элементы из последовательностей переданных в качестве аргументов'.split()

char = 'а' #Ищем этот символ

rs = list(map(lambda x: [i for i in range(len(x)) if x[i] == char],
            filter(lambda x: x.find(char) != -1, ls)))

print(rs)

