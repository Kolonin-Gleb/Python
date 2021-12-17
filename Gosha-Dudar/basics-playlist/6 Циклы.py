i = 0

while i < 10:
    print(i)
    i+=2

for j in "Hello, world":
    if j == 'a':
        #continue #Пропуск итеррации
        break #Выход из цикла
    print(j * 2, end = '') # end = '' - отмена переноса строки
else: 
    print("\nБуквы а нет в слове!")



    