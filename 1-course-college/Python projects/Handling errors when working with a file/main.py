fileName = input("Введите имя файла в формате имя.txt: ")

try:
    f = open(fileName, 'r', encoding='utf-8') 
except:
    print("Ошибка открытия файла!")
else:
    print("Файл успешно открыт.")

try:
    textFromFile = f.read()
except:
    print("Ошибка чтения файла!")
else:
    print("Файл успешно прочитан.")

# problems
try:
    f.seek(0)
    f.readline() # lines numiration begins with 0 line, I want to go to "2" line
except:
    print("Ошибка чтения 1 строки / перехода на следующую строку файла!")
else:
    print("Чтение 1 строки / перехода на следующую строку файла было выполнено успешно.")

try:
    textFromFile = f.read() # I have to read file from second line
except:
    print("Ошибка записи данных из файла со 2 строки в переменную!")
else:
    print("Данные из файла со 2 строки были успешно записаны в переменную.")

try:
    print(textFromFile)
except:
    print("Ошибка вывода данных из переменной!")
else:
    print("Вывод данных из переменной выполнен успешно.")

try:
    f.close()
except:
    print("Ошибка закрытия файла!")
else:
    print("Файл успешно закрыт.")
