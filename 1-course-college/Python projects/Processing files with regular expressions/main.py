import re

draftLs = []
eventsLs = []

with open('train_trip_log.txt', 'r', encoding='utf-8') as f:
	for line in f.readlines():
		if line[0] == '○':
			draftLs.append(line)

for line in draftLs:
	#Записываем время и номер поезда
	timeAndTrainNumber = re.findall(r'\d\d:\d\d:\d\d', line)[0] + ' - Поезд № ' + re.findall(r'\d+\b', re.findall(r'Рейс \d+\b', line)[0])[0]

	#Выбираем куда\из отправился

	#1 Выбираем буквы
	destination = re.findall(r'[А-Яа-я]+', line)
	#2 Выбираем нужный текст и составляем сообщение
	eventData = timeAndTrainNumber + " " + destination[-3] + " " + destination[-2]
	
	eventsLs.append(eventData)
	
with open('events.txt', 'w', encoding='utf-8') as f:
	for event in eventsLs:
		f.write(event + '\n')
