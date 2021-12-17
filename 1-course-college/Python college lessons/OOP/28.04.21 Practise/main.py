class Point:

    def __init__(self, x, y):
        self.__x = x #Incapsulation #age is private now
        self.__y = y

    def __str__(self): # priority 1 # is used to output object as a string 
        return f'Я - точка: {self.__x} X {self.__y}!'

    def move_to(self, new_x, new_y):
        self.__x = new_x
        self.__y = new_y

    def move_by(self, movement_x, movement_y):
        self.__x += movement_x
        self.__y += movement_y

#getters and setters as methods
    # def get_x(self):
    #     return self.__x
    #
    # def get_y(self):
    #     return self.__y
    #
    # def set_x(self, x):
    #     self.__x = x
    #
    # def set_y(self, y):
    #     self.__y = y

    #getters and setters as properties
    # They must have the same names!

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
            self.__x = x
    
    @y.setter
    def y(self, y):
            self.__y = y
    

#methods test
p = Point(0, 0)
print(p)
p.move_to(10, 10)
print(p)
p.move_by(-5, -5)
print(p)

#getters and setters as methods test
# print("Текущая координата х = " + str(p.get_x()) )
# print("Текущая координата y = " + str(p.get_y()) )
#
# p.set_x(24)
# p.set_y(24)
# print(p)

#getters and setters as properties test
print("Текущая координата х = " + str(p.x) )
print("Текущая координата y = " + str(p.y) )

p.x = 24
p.y = 24
print(p)

