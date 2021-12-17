# Декоратор для функции
def decorator(func):
    def wrapper (): # Обертка
        print("Код до выполнения функции")
        func()
        print("Код после выполнения функции")
    return wrapper #Возращаем функцию, но () не ставим

@decorator # Применяем декоратор к функции
def show():
    print("Я обычная функция")

show()

