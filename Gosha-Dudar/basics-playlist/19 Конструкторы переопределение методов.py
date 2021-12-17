class Person:
    # Поля данных
    name = 'newPerson' # Имя по умолчанию
    age = 0

    # Методы
    def info(self): #В каждом методе должен присутствовать аргумент self
        # self означает, что метод вызывается для вызывающего объекта
        print('age = ' + str(self.age))
        print('name = ' + str(self.name))

    # Конструкторы

    def __init__(self, name, age):
        self.age = age
        self.name = name

class Student(Person):
    course = 0

    # Переопределенный метод
    def info(self):
        print('age = ' + str(self.age))
        print('name = ' + str(self.name))
        print('course = ' + str(self.course))

Gleb = Student('Gleb', 18)
Gleb.course = 1
Gleb.info()

