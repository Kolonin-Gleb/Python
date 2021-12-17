# ������ �  �������


# �������� 


# r - read
# r+ - read and write
# w - write � ��������
# w+ - write and read
# a - ���������� ���� � �����
# a+ - ������ � ������ ��� �������


# ���������� ������

#f = open('file.txt', 'r+', encoding='utf-8') 

#textFromFile = f.read()

#print(textFromFile)

#f.close()

#with open('file.txt', 'r+', encoding='utf-8') as f: # ������ ����������� ���� ������� ����
##	text = f.read(4) # ������ ������ 4 �������
##	text_another = f.read(3) # ������ ��������� 3 �������
#	line = f.readline() # ������ ������

#print(line)
#print(text)
#print(text_another)

with open('file.txt', 'r', encoding='utf-8') as f:
	#lines = f.readlines()
	#for line in lines:
	#	print(line)

	for line in f:
		print(line)


# ���������� ������

#with open('file.txt', 'r+', encoding='utf-8') as f:
#	f.write("\nHello")


#with open('file.txt', 'a+', encoding='utf-8') as f: 
#	print(f.tell())
#	text = f.read(5)
#	f.seek(15)



