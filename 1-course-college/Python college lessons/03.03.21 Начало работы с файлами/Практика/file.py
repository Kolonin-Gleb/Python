with open('test.txt', 'w', encoding='utf-8') as f:
	for i in range(1, 16):
		f.write('String number ' + str(i) + '\n')

with open('test2.txt', 'w', encoding='utf-8') as f2:
	f = open('test.txt')
	for line in f:
		if strNum % 3:
			continue
		else:
			f2.write(f.readline())
	strNum +=1
	f.close()
