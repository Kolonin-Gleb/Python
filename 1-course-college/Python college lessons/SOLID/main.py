# Программисты придумали принципы написания хорошоего кода.
# Придерживаясь данных принципов получается писать более качественный и удобочитаемый код.
#   Популярные принципы:
# YAGNI ("You aren't gonna need it") или не пиши код, который тебе не нужен
# DRY ("don't repeat yourself") или не пиши код, который уже написан
# SOLID:
# S - SRP - Single Responsibility Principle - Принцип Единой Ответственности
# O - OCP - Open-closed Principle - Принцип открытости/закрытости
## L - LSP - Liskov Substitution Principle
## I - ISG - Interface Segregation Principle
## D - DIP - Dependency Inversion Principle

# Разберем первые два пункта данного принципа:

# S - Принцип Единой Ответственности.
# Он гласит, что каждая функция или метод должны делать строго определенную вещь и ничего больше
# Т.е. не нужно писать огромную функцию, которая выполняет кучу разных действий.
# Нужно писать много функций, которые будут выполнять маленькие части задачи.
#   P.S Это позволит использовать их для решения других задач в будущем.

def findSumOfDigitsInFactorialOfANumber(num): # Плохо, функция многозадачна
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i +=1
    
    result = 0
    while factorial > 0:
        result += factorial % 10
        factorial //= 10

    return result

print(findSumOfDigitsInFactorialOfANumber(10))

# Две функции дополняющие друг друга - хорошо!
def factorial(num):
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i +=1

    return factorial

def findSumOfDigits(num):
    result = 0
    while num > 0:
        result += num % 10
        num //= 10

    return result

print(findSumOfDigits(factorial(10)))


# O - Принцип открытости/закрытости
# Он гласит, что 
# Программные сущности должны быть открыты для добавления функционала, но закрыты для его изменения.
# Соблюдение данного принципа позволяет не переписывать уже написанный код, а лишь дописывать новый.
# По этой же причине тестировщикам ПО не придется тестировать немного измененный код, что тестировался ранее.

# Давайте представим, что у вас есть магазин, и вы даете скидку в 20% для ваших любимых покупателей
# используя класс Discount.
# Если бы вы решаете удвоить для VIP клиентов, вы могли бы изменить класс следующим образом:

class Discount:
  def __init__(self, customer, price):
      self.customer = customer
      self.price = price
  def give_discount(self):
      if self.customer == 'fav':
          return self.price * 0.2
      if self.customer == 'vip':
          return self.price * 0.4

# Но нет, это нарушает OCP.
# Например, если мы хотим дать новую скидку для другого типа
# покупателей, то это требует добавления новой логики. Чтобы следовать OCP, мы добавим новый класс,
# который будет расширять Discount. И в этом новом классе реализуем требуемую логику:

class Discount:
    def __init__(self, customer, price):
      self.customer = customer
      self.price = price
    def get_discount(self):
      return self.price * 0.2

class VIPDiscount(Discount):
    def get_discount(self):
      return super().get_discount() * 2


