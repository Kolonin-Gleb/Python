# r - read
# r+ - read and write
# w - write � ��������
# w+ - write and read
# a - ���������� ���� � �����
# a+ - ������ � ������ ��� �������

f = open('text.txt', 'r+', encoding='utf-8') 
textFromFile = f.read()
print(textFromFile)

f.close()