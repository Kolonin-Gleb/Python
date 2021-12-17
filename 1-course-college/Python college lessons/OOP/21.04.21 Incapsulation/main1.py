class Hippo:
    #service methods are written with __ before and after the name of the method

    def __init__(self, age, name, size):
        self.__age = age #Incapsulation #age is private now
        self.name = name
        self.size = size
        self.sound = 'Мууу'

    def __del__(self):
        print("I am dead!")


    def __repr__(self): # priority 2 #make string
        return f'My name is {self.name}, My age is {self.__age}'
    
    def __str__(self): # priority 1 # is used to output object as a string 
        return f'My name is {self.name}, My age is {self.__age}!'

    def eat(self):
        print(f'hippo {self.name} is eating')

    def make_sound(self):
        print(self.sound)

    def getting_older(self):
        self.__age += 1 

#getters and setters

    # def get_age(self):
    #     return self.__age

    # def set_age(self, age):
    #     self.__age = age

#getters and setters analog

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, v):
        if v > 0:
            self.__age = v
        else:
            print("Возраст не может быть отрицательным")


# hippo = Hippo(24, 'Gogl', 'huge')

# print("hippo data: ")
# print(hippo.age)
# print(hippo.name)
# print(hippo.size)

# print('___________________')

# hippo.eat()
# hippo.make_sound()
# hippo.getting_older()

# print("hippo data: ")
# print(hippo.age)
# print(hippo.name)
# print(hippo.size)

hippo = Hippo(24, 'Gogl', 'huge')

print(hippo)

# Incapsulation 
# there is no acess modificators in python!

# #getters and setters use
# print(hippo.get_age())
# hippo.set_age(0)
# print(hippo.get_age())

print(hippo.age) #not hippo.age()
hippo.age = 25 #call for setter 

print(hippo.age)

