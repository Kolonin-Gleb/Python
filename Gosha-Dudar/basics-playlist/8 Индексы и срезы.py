l = [34, 'ssd', 24, 17]

i = 0
while i < len(l):
    print(l[i])
    i+=1

# Для создания срезов (выборки опр. значений) 
# из списка, нужно указывать аргументы в следующем порядке:
# object[start:stop:step]

family = ["Gleb", "Lev", "Semyon", "Sveta"]

print("Обычный вывод списка " + str(family))
print("Срез. Только родители " + str(family[2::]))
print("Срез. Только дети " + str(family[:2]))
print("Срез. Список наоборот " + str(family[::-1]))


