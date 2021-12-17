with open('test.txt', 'wt', encoding='utf-8') as f:
    num = int(input()) # Т.к. я использую менеджеры with as,
    # даже при возникновении ошибки файл корректно закроется
    line = str('1 / ' + str(num) + ' = ' + str(1 / num))
    f.write(line)