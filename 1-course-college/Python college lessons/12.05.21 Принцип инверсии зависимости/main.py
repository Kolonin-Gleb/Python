#Принцип инверсии зависимости

from random import randint
import abc #Помогает с созданием абстракций

class IReader(abc.ABC):
    @abc.abstractclassmethod
    def read(self):
        pass

class FileReader:
    def read(self):
        return str(randint(1, 1000))

###

class IWriter(abc.ABC): #Создание абстрактного класса
    @abc.abstractclassmethod
    def write(self, msg):
        pass

class FileWriter(IWriter):
    def write(self, msg):
        print("Записано в файл: ")
        print(msg)

class DBWriter(IWriter):
    def write(self, msg):
        print("Записано в БД: ")
        print(msg)

class Process:
    def __init__(self, reader, writer):
        
        if not isinstance(reader, FileReader):
            raise Exception("Ошибка при чтении файла")
        if not isinstance(writer, IWriter): #Зависим от интерфейса (Абстракции)
            raise Exception("Ошибка при записи")
        
        self._writer = writer
        self._reader = reader

    def process(self):
        v = self._reader.read()
        self._writer.write(v)

r = FileReader()
w = FileWriter()
dbw = DBWriter()


p = Process(r, w)
p.process()

p1 = Process(r, dbw)
p1.process()
