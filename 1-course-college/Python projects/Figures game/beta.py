from random import randint
import os


class Game:
    userSol = "Y"

    def __init__(self):
        os.system("cls")
        print("\t\t Игра угадай площадь фигуры.")
        print("Если в ответе получается дробное число, отбросьте часть после запятой без округления")


    def play_or_stop(self):
            print("Хотите сыграть? (Y/N)")
            Game.userSol = input().capitalize()

    def __del__(self):
        os.system("cls")
        print('Спасибо за игру!')
    
class Figure:

    def __init__(self):
        self.area = 0
        self.perimeter = 0

    #getters
    @property
    def get_area(self):
        return self.area
    
    @property
    def get_perimeter(self):
        return self.perimeter

    def get_user_guess_area(self):
        print("Введите мою площадь: ")
        area_guess = int(input())
        return area_guess

    def get_user_guess_perimeter(self):
        print("Введите мой периметр: ")
        perimeter_guess = int(input())
        return perimeter_guess

class Circle(Figure):
    class_name = 'круг'

    def __str__(self):
        return f'Я - {self.class_name} c радисусом = {self.radius}'

    def __init__(self, radius): #new constructor
        super().__init__() #parent's constructor
        self.radius = radius
        self.area = int(3.14 * radius**2)
        self.perimeter = int(2 * 3.14 * radius)

    

class Rectangular(Figure):
    class_name = 'прямоугольник'
    
    def __str__(self):
        return f'Я - {self.class_name} cо сторонами 1 = {self.side1} 2 = {self.side2}'

    def __init__(self, side1, side2):
        super().__init__()
        self.side1 = side1
        self.side2 = side2

        self.area = side1 * side2
        self.perimeter = (side1 + side2) * 2

class Triangle(Figure):
    class_name = 'треугольник'

    def __str__(self):
        return f'Я - {self.class_name} cо сторонами: \n1 = {self.side1} 2 = {self.side2} 3 = {self.side3}'

    def __init__(self, side1, side2, side3):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


        self.perimeter = side1 + side2 + side3
        self.area = int((self.perimeter / 2 * (self.perimeter / 2 - side1) * (self.perimeter / 2 - side2) * (self.perimeter / 2 - side3)) ** 0.5)

#Чтобы не создавать несуществующие треугольники
def create_triangle():
    while True:
        a = randint(1, 10)
        b = randint(1, 10)
        c = randint(1, 10)

        if a + b > c and a + c > b and b + c > a:
            break

    return [a, b, c]



game = Game()

while True:
    game.play_or_stop()
    os.system("cls")
    if game.userSol == 'N':
        break

    rand_figure = randint(1, 3)

    if rand_figure == 1: #Circle
        radius = randint(1, 10)
        circle = Circle(radius)
        print(circle)

        if circle.area == circle.get_user_guess_area():
            print("Верно!")
        else:
            print("Неверно! Правильный ответ = " + str(circle.area))
            continue
        if circle.perimeter == circle.get_user_guess_perimeter():
            os.system("cls")
            print("Верно!")
        else: 
            print("Неверно! Правильный ответ = " + str(circle.perimeter))
            continue

    elif rand_figure == 2: #Rectangular
        rectangular = Rectangular(randint(1, 10), randint(1, 10))
        print(rectangular)

        if rectangular.area == rectangular.get_user_guess_area():
            print("Верно!")
        else:
            print("Неверно! Правильный ответ = " + str(rectangular.area))
            continue
        if rectangular.perimeter == rectangular.get_user_guess_perimeter():
            os.system("cls")
            print("Верно!")
        else: 
            print("Неверно! Правильный ответ = " + str(rectangular.perimeter))
            continue

    else: #Triangle
        sides = create_triangle()
        triangle = Triangle(sides[0], sides[1], sides[2])
        print(triangle) # Если стороны = 6 4 10 , то s = 0

        if triangle.area == triangle.get_user_guess_area():
            print("Верно!")
        else:
            print("Неверно! Правильный ответ = " + str(triangle.area))
            continue
        if triangle.perimeter == triangle.get_user_guess_perimeter():
            os.system("cls")
            print("Верно!")
        else: 
            print("Неверно! Правильный ответ = " + str(triangle.perimeter))
            continue

del game

