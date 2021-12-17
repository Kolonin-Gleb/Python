class Person:
    name = 'newPerson' # Имя по умолчанию
    age = 0

    # Пример Инкапсуляции 2
    # В python нет модификаторов доступа

    # _ - Совет не использовать данное поле данных у наследников
    # _nationality = 'undefined'

    # __ - запрет использовать данное поле данных у наследников
    # Его можно обойти!
    __nationality = 'undefined'



    def info(self): #В каждом методе должен присутствовать аргумент self
        # self означает, что метод вызывается для вызывающего объекта
        print('age = ' + str(self.age))
        print('name = ' + str(self.name))

# Пример наследования 1
class Student (Person): # В () от кого наследуем поля и методы
    course = 1 # Курс по умолчанию

# Vlad = Person() #Создание объекта
# Vlad.name = 'Vlad'
# Vlad.age = 2

# Vlad.info()

Igor = Student()

Igor.info()
print(Igor.course)

# print(Igor._nationality) # ok 
# print(Igor.__nationality) # error 
print(Igor._Person__nationality) # ok 

