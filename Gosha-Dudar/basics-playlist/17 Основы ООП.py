class Person:
    name = 'newPerson' # Имя по умолчанию
    age = 0

    def info(self): #В каждом методе должен присутствовать аргумент self
        # self означает, что метод вызывается для вызывающего объекта
        print('age = ' + str(self.age))
        print('name = ' + str(self.name))

Vlad = Person() #Создание объекта
Vlad.name = 'Vlad'
Vlad.age = 2

Vlad.info()
