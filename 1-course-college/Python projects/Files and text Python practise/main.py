import functions

uniqueWords = functions.readFile('data.txt')

uniqueWords = list(uniqueWords)

functions.saveDataToFile(uniqueWords, 'unique data.txt')
