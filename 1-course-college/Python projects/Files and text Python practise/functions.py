def readFile(fileName):

    uniqueWords = set() #Пустое множество уникальных слов

    with open(fileName, 'r', encoding='utf-8') as fData:
        lines = fData.readlines()
        for line in lines:
            line = line.lower()

            # Убираем пунктуацию
            if line.find(","):
                line = line.replace(",", "")
            if line.find("."):
                line = line.replace(".", "")
            if line.find(" - "): #Тире является пункуационным знаком
                line = line.replace(" - ", " ")

            lineList = line.split() #Разбиваем строку на слова и заносим их в список

            uniqueWords = uniqueWords.union(set(lineList)) #Сохраняем только уникальные слова  
    return uniqueWords

def saveDataToFile(dataList, fileName):

    dataList.sort()

    with open(fileName, 'w', encoding='utf-8') as f:
        f.write("Всего уникальных слов - " + str(len(dataList))  + '\n')
        f.write("==============================\n")

        for word in dataList:
            f.write(word + "\n")