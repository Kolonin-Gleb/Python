#Списки в python - массивы способные
#хранить разные типы данных

# list = ['G', 1, 5, 'x', 3.14, ['S', 'p', 'a', 'c', 'e']]

# print("list is printing: " + str(list))

# #pos. indexes    0    1    2
# list2        = ['0', '1', '2']
# #neg. indexes    -3   -2   -1
# print(list2[-1])

# list2.append('3') #Добавление эл. в конец списка

# print(list2)

# list2.extend(list) #Добавление всех эл. преданного списка в конец вызывающего метод списка

# print(list2)



#          0  1
# myList = [1, 2, 3, 2, 1, ['S', 'p', 'a', 'c', 'e', 1]]

# myList.insert(-1, 'X') #Вставка элемента по индексу. Вставить элемент в список в списке не получится

# print(myList)

# myList.remove(2) #Удаление первого элемента, соответствующего значению

# print(myList)

# print(myList.pop()) #Удаление эл. по индексу. Елси не указывать индекс, то будет удален последний эл.

# print(myList.index(1)) #Возращает индекс первого эл. соответствующего значению. Эл. во вложенных списках не находит

# print(myList.count(1)) #Возращает кол. эл. имеющих переданное значение. Эл. во вложенных списках не находит


listOfNums = [1, 4, 3, 7, 2]
print(listOfNums)
listOfNums.sort() #Сортировка (по умолчанию - по возрастанию)
print(listOfNums)

listOfLetters = ['b', 'd', 'a', 'c']
print(listOfLetters)
listOfLetters.sort() #Сортировка (по умолчанию - по алфавиту)
print(listOfLetters)

listOfNums.reverse() #Переворот списка
print(listOfNums)

listOfLetters.clear() #Очистка содержимого списка
print(listOfLetters)

