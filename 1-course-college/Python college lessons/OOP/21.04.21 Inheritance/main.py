#Inheritance

class Car:
    def __init__(self, color, year, mileage):
        self.color = color
        self.year = year
        self.mileage = mileage
        self.state = False

    def __str__(self):
        return f'Car data: color - {self.color}, year - {self.year}, mileage - {self.mileage}.'

    def start(self):
        if state == True:
            self.state = True
            print("Car started up")

    def stop(self):
        if state == True:
            self.state = False
            print("Car stopped")

    def ride(self):
        print("Ride")

class Passenger_car (Car): #Inheritance ex
    
    #constructor reload
    def __init__(self, color, year, mileage, passanger_capacity):
        super().__init__(color, year, mileage)
        self.passanger_capacity = passanger_capacity

    def register_passanger(self):
        print("Passanger has been registred")

    def ride(self): #method reload
        super().ride() # Use parent's method realization
        print("Go go go!") #add new realization



# car = Car('red', 2021, 100)
# print(car)
# car.ride()

# print("\n")

p_car = Passenger_car('blue', 2000, 717451345, 5)
print(p_car)
print(p_car.passanger_capacity)

# p_car.register_passanger()
# p_car.ride()

