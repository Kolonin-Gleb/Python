# Есть массив из целых положительных чисел.
# Написать функцию, которая определяет можно ли заданное число представить суммой чисел из массива
# (каждое число можно использовать один раз):
# Пример: Массив: {1, 7, 9} Число 10 - можно представить суммой (1 + 9) Число 5 - нельзя


def isNumFromSumOfListElements(num, ls):
    originNum = num

    ls.sort(reverse=True) #from big to small

    print(ls)

    for i in ls:
        if num - i >= 0:
            num -= i
        else:
            continue
        if num == 0:
            break

    if num == 0:
        print(f"Число {originNum} можно получить складывая элементы списка {ls}")
        return True
    else:
        print(f"Число {originNum} невозможно получить складывая элементы списка {ls}")
        return False


numbersList = [8, 2, 1, 7, 21]
isNumFromSumOfListElements(23, numbersList)
