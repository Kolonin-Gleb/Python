#OOP

# class Person:
#     #properties
#     name = 'new person' #default name
#     age = 0
#     #methods
#     def info(self):
#         print('My name = ' + self.name)
#         print('My age = ' + str(self.age))

#     def greet(self, greeting):
#         print (str(greeting))

#     #constructors
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name

class CoffeMachine:
    #static properties
    count = 0

    # #properties
    # state = 'off'
    # model = 'unknown'
    # coffe_types_ls = []

    def __init__(self, model, *coffe_types):
        CoffeMachine.count += 1 #change static property

        self.model = model
        self.state = 'off'

        self.coffe_types_ls = list(coffe_types)

    def turn_on(self):
        if self.state != 'on':
            self.state = 'on'
            print("Activated")
        else:
            print("Already activated")

    def turn_off(self):
        if self.state != 'off':
            self.state = 'off'
            print("Defused")
        else:
            print("Already Defused")

    def create_coffe(self, coffe_type):
        if coffe_type in self.coffe_types_ls:
            print('Порошок насыпан.\n Кофе готов.\n Приятного аппетита!')
        else:
            print('Я не умею делать такой кофе')


# c_m1 = CoffeMachine('Nescaffe')

# c_m1.turn_on()
# c_m1.turn_off()
# c_m1.turn_off()

# print(c_m1.model)

# c_m2 = CoffeMachine('Bosh')

# print(c_m1.count)

# Vlad = Person('Vlad', 1) #create new object

# #use methods
# Vlad.info() 
# Vlad.greet('Hi!')

# #change properties
# Vlad.age = 2
# Vlad.info()


c_m = CoffeMachine('Nescaffe', 'cappuchino', 'black')

c_m.create_coffe('2')
c_m.create_coffe('cappuchino')


