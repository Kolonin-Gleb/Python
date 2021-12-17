try:
    age = int(input("Возраст:"))
    if age < 18:
        raise Exception("Несовершеннолетний")
except:
    print("Доступа нет!")
else:
    print("Добро пожаловать!")
